import tableauserverclient as TSC
import time
import logging

# ログの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # Tableau Server 接続の設定
    server_url = 'https://your-tableau-server'
    api_token_name = 'your-token-name'
    api_token_value = 'your-token-value'
    site_id = 'your-site-id'  # サイトID (通常は空文字 '')

    # タグの設定
    desired_tag = 'your-tag'  # ここにリフレッシュしたいデータソースのタグを指定

    # サインイン
    tableau_auth = TSC.PersonalAccessTokenAuth(token_name=api_token_name, personal_access_token=api_token_value, site_id=site_id)
    server = TSC.Server(server_url, use_server_version=True)

    max_retries = 3
    retry_delay = 5  # リトライ間隔 (秒)
    page_size = 100  # 一度に取得するデータソースの数

    def execute_with_retry(func, *args, **kwargs):
        for attempt in range(max_retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.error(f"Attempt {attempt + 1} failed: {e}")
                if attempt < max_retries - 1:
                    logger.info(f"Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                else:
                    logger.error("Max retries reached. Exiting.")
                    raise

    with server.auth.sign_in(tableau_auth):
        all_datasources = []
        pagination_item = None
        while True:
            options = TSC.RequestOptions(pagenumber=len(all_datasources) // page_size + 1, pagesize=page_size)
            datasources, pagination_item = execute_with_retry(server.datasources.get, req_options=options)
            all_datasources.extend(datasources)
            if len(all_datasources) >= pagination_item.total_available:
                break
            logger.info(f"Retrieved {len(all_datasources)} of {pagination_item.total_available} datasources...")

        logger.info(f"Total datasources found: {pagination_item.total_available}")

        # タグでフィルタリング
        tagged_datasources = [ds for ds in all_datasources if desired_tag in ds.tags]
        logger.info(f"Datasources with tag '{desired_tag}': {len(tagged_datasources)}")

        # データソースのリフレッシュ
        for datasource in tagged_datasources:
            try:
                execute_with_retry(server.datasources.refresh, datasource.id)
                logger.info(f"Datasource {datasource.name} has been refreshed successfully.")
            except Exception as e:
                logger.error(f"Failed to refresh datasource {datasource.name}: {e}")

if __name__ == '__main__':
    main()

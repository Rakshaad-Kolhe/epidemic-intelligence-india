import time

from app.ingestion.news.rss_collector import collect_rss_outbreak_signals


def run_scheduler():
    while True:
        try:
            print("Starting RSS collection...")
            collect_rss_outbreak_signals()
            print("Collection complete.")
        except Exception as exc:
            print(f"Collection failed: {exc}")

        time.sleep(1800)


if __name__ == "__main__":
    run_scheduler()

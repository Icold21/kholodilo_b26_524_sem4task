import re
import json
import logging
from collections import Counter

ACCESS_LOG = "data/access.log"
STATS_FILE = "data/stats.json"
LOG_FILE   = "data/app.log"

LOG_PATTERN = re.compile(
    r"^(?P<date>\d{4}-\d{2}-\d{2})\s+"
    r"(?P<time>\d{2}:\d{2}:\d{2})\s+"
    r"(?P<ip>\d{1,3}(?:\.\d{1,3}){3})\s+"
    r"(?P<method>[A-Z]+)\s+"
    r"(?P<url>\S+)\s+"
    r"(?P<status>\d{3})$"
)


def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE, encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )


def process_log(file_path: str) -> dict | None:
    method_counts = Counter()
    status_counts = Counter()
    url_counts = Counter()

    errors_4xx = 0
    total_lines = 0
    matched_lines = 0
    bad_lines = 0

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line_no, raw in enumerate(f, start=1):
                total_lines += 1
                line = raw.strip()
                if not line:
                    logging.debug("Line %d is empty, skipping", line_no)
                    continue

                m = LOG_PATTERN.match(line)
                if not m:
                    bad_lines += 1
                    logging.warning(
                        "Line %d does not match the format: %r", line_no, line
                    )
                    continue

                matched_lines += 1
                ip     = m["ip"]
                method = m["method"]
                url    = m["url"]
                status = int(m["status"])

                method_counts[method] += 1
                status_counts[status] += 1
                url_counts[url] += 1

                if 400 <= status < 500:
                    errors_4xx += 1

                logging.debug(
                    "Line %d: %s %s %s -> %d",
                    line_no, ip, method, url, status,
                )

    except FileNotFoundError:
        logging.error("File not found: %s", file_path)
        return None
    except PermissionError:
        logging.error("Permission denied while reading: %s", file_path)
        return None
    except UnicodeDecodeError as e:
        logging.error("Decoding error in %s: %s", file_path, e)
        return None
    except OSError as e:
        logging.error("I/O error while reading %s: %s", file_path, e)
        return None

    most_common_url = url_counts.most_common(1)[0][0] if url_counts else None

    stats = {
        "total_lines":     total_lines,
        "matched_lines":   matched_lines,
        "bad_lines":       bad_lines,
        "method_counts":   dict(method_counts),
        "status_counts":   {str(k): v for k, v in sorted(status_counts.items())},
        "errors_4xx":      errors_4xx,
        "url_counts":      dict(url_counts),
        "most_common_url": most_common_url,
    }
    return stats


def save_stats(stats: dict, output_path: str) -> None:
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)
        logging.info("Statistics saved to %s", output_path)
    except OSError as e:
        logging.error("Failed to write %s: %s", output_path, e)


def main() -> int:
    setup_logging()
    logging.info("Starting processing of %s", ACCESS_LOG)

    stats = process_log(ACCESS_LOG)
    if stats is None:
        logging.error("Processing aborted due to file read error")
        return 1

    save_stats(stats, STATS_FILE)

    logging.info(
        "Done. Lines: %d (parsed: %d, skipped: %d)",
        stats["total_lines"], stats["matched_lines"], stats["bad_lines"],
    )
    logging.info("4xx errors: %d", stats["errors_4xx"])
    logging.info("Most frequent URL: %s", stats["most_common_url"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
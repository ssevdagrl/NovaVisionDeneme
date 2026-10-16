
from collections import Counter


def count_detections(detections):
    """
    Count YOLO detection results.

    Args:
        detections: List of detected objects.

    Returns:
        Dictionary with total and class counts.
    """

    class_counts = Counter()

    for detection in detections:
        if isinstance(detection, dict):
            class_name = detection.get("class_name", "unknown")
        else:
            class_name = getattr(detection, "class_name", "unknown")

        class_counts[str(class_name)] += 1

    return {
        "total": len(detections),
        "by_class": dict(class_counts)
    }


if __name__ == "__main__":
    sample_detections = [
        {"class_name": "person"},
        {"class_name": "person"},
        {"class_name": "car"},
        {"class_name": "car"},
        {"class_name": "car"},
        {"class_name": "bicycle"}
    ]

    result = count_detections(sample_detections)
    print(result)

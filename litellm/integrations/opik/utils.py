
BLUE = "\033[94m"
RED = "\033[91m"
RESET = "\033[0m"

def pformat(text: str, level: str="info") -> str:
    """
    Format the text with colors.

    Args:
        text: the text to format
        info: the mode ("input" or "error")

    Returns a formatted string
    """
    return "%s%s%s" % (BLUE if level == "info" else RED, text, RESET)

def get_current_span_id(metadata: Dict[str, Any]) -> str:
    from opik.opik_context import get_current_span_data

    if metadata.get("current_span_data"):
        current_span_data = metadata.get("current_span_data")
    else:
        current_span_data = get_current_span_data()

    if current_span_data:
        return current_span_data.id
    else:
        return None


def get_current_trace_id(metadata: Dict[str, Any]) -> str:
    from opik.opik_context import get_current_trace_data

    if metadata.get("current_trace_data"):
        current_trace_data = metadata.get("current_trace_data")
    else:
        current_trace_data = get_current_trace_data()

    if current_trace_data:
        return current_trace_data.id
    else:
        return None


def model_response_to_dict(response_obj: ModelResponse) -> Dict:
    """
    Convert the ModelResponse to a dictionary.

    Args:
        response_obj: the ModelResponse from the model vendor, standardized

    Returns a dictionary
    """
    return response_obj.to_dict()

def redact_secrets(item):
    """
    Recursively redact sensitive information
    """
    if isinstance(item, dict):
        redacted_dict = {}
        for key, value in item.items():
            value = redact_secrets(value)
            if key == "api_key":
                value = "***REDACTED***"
            redacted_dict[key] = value
        return redacted_dict
    else:
        return item

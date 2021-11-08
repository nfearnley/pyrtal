def clamp(minVal, val, maxVal):
    """Clamp a `val` to be no lower than `minVal`, and no higher than `maxVal`."""
    return max(minVal, min(maxVal, val))

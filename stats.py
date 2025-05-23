def get_num_words(text: str) -> int:
    return len(text.split())


def get_num_characters(text: str) -> dict[str, int]:
    result = {}
    for c in text:
        lower_c = c.lower()
        if lower_c in result:
            result[lower_c] += 1
        else:
            result[lower_c] = 1
    return result


def get_sorted_characters_by_count(
    chars_num: dict[str, int],
) -> list[dict[str, object]]:
    result = []
    for c, num in chars_num.items():
        result.append({"char": c, "num": num})
    result.sort(reverse=True, key=lambda d: d["num"])
    return result

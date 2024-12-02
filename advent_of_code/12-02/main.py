def part_two(input_str: str) -> int:
    def report_is_safe(report):
        diffs = [report[i + 1] - report[i] for i in range(len(report) - 1)]

        increase = sum(1 if d > 0 else -1 for d in diffs) > 0

        follows_trend = all(d > 0 if increase else d < 0 for d in diffs)

        differs_safely = all(1 <= abs(d) <= 3 for d in diffs)

        return follows_trend and differs_safely

    count = 0

    for line in input_str.splitlines():
        report = [int(x) for x in line.split()]

        if len(report) < 2:
            continue

        if report_is_safe(report):
            count += 1
            continue

        for i in range(len(report)):
            sliced_report = report[:i] + report[i + 1:]
            if report_is_safe(sliced_report):
                count += 1
                break  

    return count

f = open("data.txt", "r")
arr = f.read()

reponse = part_two(arr)
print(reponse)

def sum_calibration_values(calibration_text):
    total_sum = 0

    calibration_lines = calibration_text.split('\n')

    for line in calibration_lines:
        # Find the first and last digits in the line
        first_digit = next((char for char in line if char.isdigit()), None)
        last_digit = next((char for char in reversed(line) if char.isdigit()), None)

        if first_digit is not None and last_digit is not None:
            total_sum += int(first_digit + last_digit)

    return total_sum

# Example usage
calibration_text = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

result = sum_calibration_values(calibration_text)
print(result)

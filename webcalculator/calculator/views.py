from django.shortcuts import render


def index(request):
    result = None
    error = None

    if request.method == "POST":
        try:
            num1 = float(request.POST.get("num1"))
            num2 = float(request.POST.get("num2"))
            operator = request.POST.get("operator")

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    error = "除数不能为 0"
                else:
                    result = num1 / num2
            else:
                error = "请选择正确的运算符"

            # 如果结果是整数，就显示成整数，避免出现 2.0
            if result is not None and isinstance(result, float) and result.is_integer():
                result = int(result)

        except (TypeError, ValueError):
            error = "请输入有效的数字"

    return render(
        request,
        "calculator/index.html",
        {
            "result": result,
            "error": error,
        },
    )

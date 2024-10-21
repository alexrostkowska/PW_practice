# import os
# import pathlib
# import pytest 

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     screen_file = ""
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     working_root = pathlib.Path().resolve() #This line here
#     if report.when == "call":
#         if report.failed and "page" in item.funcargs:
#             page = item.funcargs["page"]
#             screenshot_dir = pathlib.Path(working_root , "report/screenshots") #This line here
#             screenshot_dir.mkdir(exist_ok=True)
#             screen_file = str(f"{slugify(item.nodeid)}.png")
#             img_path = os.path.join(screenshot_dir, screen_file) #This line here
#             page.screenshot(path=img_path)
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # add the screenshots to the html report
#             extra.append(pytest_html.extras.image(img_path))
#         report.extra = extra
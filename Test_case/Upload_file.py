file_input=
file_input.set_input_files("filename.extension")


with page.expect_file_chooser() as fc_info:

    file_input.click()
    file_chooser=fc_info.value
    file_chooser.set_files("filename.extension")


    page.goto("https://staging.quicksync.pro/", wait_until='load')
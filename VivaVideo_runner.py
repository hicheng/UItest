#coding=utf-8
import os
import time
import unittest
from iOS import script_ultils as sc, HTMLTestRunner
from iOS.VivaVideo.test_ahead import test_login
from iOS.VivaVideo.test_creations import test_settings,test_export,test_gallery,test_home,test_material



def All_TestCases():
    # #设置每个类中case的执行顺序
    # suite = unittest.TestSuite()
    # suite.addTest(Home.Home("test_home_001"))
    # suite.addTest(Home.Home("test_home_002"))
    # suite.addTest(Home.Home("test_home_003"))
    # ...
    # return suite
    #
    # #一次执行多个py文件，顺序随机执行
    # # 用例路径
    # TestCase_path = os.path.join(os.getcwd(), "TestCase")
    # # 报告存放路径
    # Report_path = os.path.join(os.getcwd(), "Report")
    #
    # def TestCase_All():
    #     Discover = unittest.defaultTestLoader.discover(TestCase_path, pattern="*.py", top_level_dir=None)
    #     return Discover

    # 用例路径
    preview_path = os.path.join(os.getcwd(), "iOS/VivaVideo/test_creations/test_preview")
    camera_path = os.path.join(os.getcwd(), "iOS/VivaVideo/test_creations/test_camera")
    edit_path = os.path.join(os.getcwd(), "iOS/VivaVideo/test_creations/test_edit")
    publish_path = os.path.join(os.getcwd(), "iOS/VivaVideo/test_creations/test_publish")

    #设置每个py文件中类的执行顺序
    file0 = unittest.TestLoader().loadTestsFromTestCase(test_login.TestUserLogin)
    file1 = unittest.TestLoader().loadTestsFromTestCase(test_settings.Settings)
    file2 = unittest.TestLoader().discover(camera_path, pattern="*.py", top_level_dir=None)
    file3 = unittest.TestLoader().loadTestsFromTestCase(test_home.TestHome)
    file4 = unittest.TestLoader().discover(edit_path, pattern="*.py", top_level_dir=None)
    file5 = unittest.TestLoader().discover(preview_path, pattern="*.py", top_level_dir=None)
    file6 = unittest.TestLoader().loadTestsFromTestCase(test_gallery.TestGallery)
    file7 = unittest.TestLoader().loadTestsFromTestCase(test_material.TestCreationTemplate)
    file8 = unittest.TestLoader().loadTestsFromTestCase(test_export.TestCreationExport)
    file9 = unittest.TestLoader().discover(publish_path,pattern="*.py", top_level_dir=None)

    suite = unittest.TestSuite([file0,file1,file2,file3,file4,file5,file6,file7,file8,file9])
    return suite

if __name__ == '__main__':
    print("开始测试")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    now_time = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    report_path = sc.path_lists[2]
    filename = report_path + now_time + ".html"
    fp = open(filename, 'wb+')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='VivaVideo UI 测试结果',
        description='详细测试报告',
        verbosity = 2
    )
    runner.run(All_TestCases())
    fp.close()
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("测试结束")
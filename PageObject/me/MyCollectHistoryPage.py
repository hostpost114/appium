from PageObject import Pages


class MyCollectHistoryPage:
    '''
    我的收藏浏览历史
    isOperate: 操作失败，检查点就失败,kwargs: WebDriver driver, String path(yaml配置参数)
    '''

    def __init__(self, **kwargs):
        self.driver = kwargs["driver"]
        self.path = kwargs["path"]
        self.page = Pages.PagesObjects(driver=self.driver, path=kwargs["path"], launch_app=1)

    def operate(self, logTest):  # 操作步骤
        self.page.operate(logTest)

    def checkPoint(self, caseName, logTest, devices):  # 检查点
        self.page.checkPoint(caseName=caseName, logTest=logTest, devices=devices)


if __name__ == "__main__":
    pass

from selenium import webdriver


driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(20)

driver.get('https://www.vmall.com/')

# 点击连接，打开新的窗口
driver.find_element_by_css_selector("div.s-sub a[href*='consumer.huawei']").click()

# 先试试，如果不点击 更多精彩会是什么结果
# 发现必须要点击， 不然selenium.common.异常.ElementNotVisibleException
# 后面再讲解，怎么移动到这个元素上，而不去点击它
driver.find_element_by_css_selector("div.s-sub    a.icon-dropdown").click()
driver.find_element_by_css_selector("a[href*='appstore.huawei.com']").click()


def checkHuawei():
    expected = '智能手机|笔记本&平板|穿戴设备|智能家居|更多产品|软件应用|服务与支持|华为商城'

    # 注意窗口的宽度决定显示多少个菜单，可能需要拉宽窗口
    # 先不写下面的代码，发现错误再添加
    size = driver.get_window_size()
    driver.set_window_size(1020, size['height'])

    # 先试着用 #cbg-main-nav  ul >li[class] 但是正好其中一个没有class
    # 只好是前面七个元素
    # 可以是 #cbg-main-nav  ul >li:nth-child(-n+7)  根据
    # http: // www.w3school.com.cn / cssref / selector_nth - child.asp
    eles = driver.find_elements_by_xpath("//div[@id='normal_nav']//li[position()<=8]")
    eleTexts = [ele.text for ele in eles]
    # 先打印看看
    for ele in eles:
        print(ele.text)
    actual = '|'.join(eleTexts)
    if actual == expected:
        print('huawei page pass')
    else:
        print('huawei page fail!!!!')


def checkAppmarket():
    expected = u'''首页|游戏|软件|专题|品牌专区|华为软件专区'''

    eles = driver.find_elements_by_css_selector("ul.ul-nav   li")
    eleTexts = [ele.text for ele in eles]
    actual = '|'.join(eleTexts)
    if actual == expected:
        print('app page pass')
    else:
        print('app page fail!!!!')


def checkVmall():
    expected = u'''平板电脑|笔记本电脑|笔记本配件'''
    from selenium.webdriver.common.action_chains import ActionChains
    ac = ActionChains(driver)

    # 演示的时候，单步调试， 停在这里
    ac.move_to_element(driver.find_element_by_id('zxnav_1')).perform()

    # 用 setTimeout(function(){debugger;},3000) 来 查看元素
    # 分析 得知  zxnav_1 ，2,3,4  分别就是对应 菜单的，里面有隐藏菜单
    eles = driver.find_elements_by_css_selector('#zxnav_1 li.subcate-item')
    eleTexts = [ele.text for ele in eles]
    actual = '|'.join(eleTexts)
    if actual == expected:
        print('main page pass')
    else:
        print('main page fail!!!!')


mainWindow = driver.current_window_handle

for handle in driver.window_handles:
    # 切换到新窗口
    driver.switch_to.window(handle)
    # 检查是否是我们要进入的window
    if '消费者业务官网' in driver.title:
        checkHuawei()
    elif '应用市场' in driver.title:
        checkAppmarket()
    elif '商城官网' in driver.title:
        checkVmall()



input('\npress to quit...')
driver.quit()

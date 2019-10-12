from selenium import webdriver
import time

class SelUtil(object):

    def __init__(self):
        # 创建浏览器对象
        self.driver = webdriver.Firefox()
        # 设置隐式等待
        self.driver.implicitly_wait(5)
        # 设置浏览器的最大化
        self.driver.maximize_window()
    
    def open_url(self):
        # 请求网址
        self.driver.get(url)
        time.sleep()
    
    def locate_element(self, local_type, value):

        el = None
        if local_type == 'id':
            el = self.driver.find_element_by_id(value)
        elif local_type == 'name':
            el = self.driver.find_element_by_name(value)
        elif local_type == 'class':
            el = self.driver.find_element_by_class_name(value)
        elif local_type == 'text':
            el = self.driver.find_element_by_link_text(value)
        elif local_type == 'xpath':
            el = self.driver.find_element_by_xpath(value)
        elif local_type == 'css':
            el = self.driver.find_element_by_css_selector(value)

        if el is not None:
            return el
        else:
            raise Exception('el is None!')

    # 对某个元素执行点击操作
    def click_element(self, local_type, value):
        # 定位元素
        el = self.locate_element(local_type, value)
        # 点击操作
        el.click()
        time.sleep(1)
    
    # 数据输入
    def data_input(self, local_type, value, data):
        # 定位元素
        el = self.locate_element(local_type, value)
        # 输入数据
        el.send_keys(data)
    
    # 获取文本
    def get_text(self, local_type, value):
        # 定位元素
        el = self.locate_element(local_type, value)
        # 获取文本
        t = el.text
        return t
    
    # 获取属性
    def get_attr(self, local_type, value):
        # 定位元素
        el = self.locate_element(local_type, value)
        # 获取属性值
        attr = el.get_attribute(data)
        return attr
    
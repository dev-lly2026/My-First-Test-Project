from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("正在启动浏览器...")
driver = webdriver.Edge()
driver.implicitly_wait(5)

try:
    print("正在打开百度...")
    driver.get("https://www.baidu.com")
    driver.maximize_window()
    
    # 等待页面主体加载完成
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    print("页面加载完成，准备执行搜索...")
    print("当前页面标题（搜索前）:", driver.title)

    # 使用JavaScript方案
    print("正在输入搜索内容...")
    driver.execute_script('document.getElementById("kw").value = "软件测试自学";')
    
    print("正在点击搜索按钮...")
    driver.execute_script('document.getElementById("su").click();')

    # 等待页面标题发生变化（核心验证点）
    print("等待搜索结果页加载...")
    wait.until(
        lambda d: d.title != "百度一下，你就知道"  # 等待标题不再是首页标题
    )
    print("当前页面标题（搜索后）:", driver.title)

    # 进一步验证：检查页面是否包含“搜索工具”等结果页元素
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "搜索工具")))
    print("✅ 搜索结果页验证通过，页面已成功跳转！")

except Exception as e:
    print(f"执行过程中出现错误: {str(e)}")

finally:
    print("正在关闭浏览器...")
    driver.quit()
    print("浏览器已关闭，程序结束")
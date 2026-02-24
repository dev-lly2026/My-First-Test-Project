# 百度搜索自动化测试项目

一个基于 Python + Selenium 的 Web UI 自动化测试实践项目，用于验证百度搜索功能的完整流程。

## 📋 项目概述
本项目通过自动化测试脚本模拟用户在百度搜索的全过程，涵盖页面导航、元素定位、数据输入、操作执行及结果验证等关键测试环节，是学习软件测试自动化技术的入门实践。

## 🛠️ 技术栈
- **编程语言**: Python 3.14.3
- **自动化框架**: Selenium WebDriver 4.x
- **浏览器**: Microsoft Edge
- **开发工具**: VS Code / 任意文本编辑器

## ✨ 功能特性
- ✅ **自动化流程**：从打开浏览器到关闭浏览器的完整自动化
- ✅ **智能等待**：结合显式等待与隐式等待，确保页面元素加载完成
- ✅ **健壮性处理**：使用 JavaScript 执行关键操作，规避常见元素交互异常
- ✅ **详细日志**：每一步操作都有清晰的控制台输出，便于调试
- ✅ **结果验证**：自动验证页面标题变化，确保测试有效性

## 🚀 快速开始

### 环境准备
1. **安装 Python 3.14.3**
   - 从 [Python官网](https://www.python.org/downloads/) 下载安装
   - 安装时务必勾选 "Add Python to PATH"

2. **安装依赖库**
   ```bash
   pip install selenium
   ```

### 配置浏览器驱动
   查看 Edge 浏览器版本：在地址栏输入 edge://version/
   从 Microsoft Edge WebDriver 下载对应版本的 msedgedriver.exe
   将 msedgedriver.exe 放入 Python 安装目录的 Scripts 文件夹

### 运行测试
   1.克隆或下载本项目
   2.打开命令行，进入项目目录
   3.执行测试脚本：python test_baidu.py


### 预期输出
🚀 自动化搜索测试开始...
==
1️⃣ 打开百度首页...
✅ 页面打开成功，当前标题：百度一下，你就知道
2️⃣ 执行搜索操作...
📝 使用 JavaScript 输入搜索词...
🔍 使用 JavaScript 点击搜索按钮...
3️⃣ 验证搜索结果...
✅ 搜索成功！当前标题：软件测试自学_百度搜索
🎉 测试执行成功！所有步骤均通过。
## 📁 项目结构
```
MyFirstTest/
├── test_baidu.py # 主测试脚本
├── README.md # 项目说明文档
├── screenshots/ # 测试截图目录
```

## 🎯 学习收获
通过本项目的实践，我掌握了以下技能：
- Selenium WebDriver 的基本原理与使用方法
- Python 编写自动化测试脚本的完整流程
- 元素定位策略：ID、CSS 选择器、XPath 等
- 等待机制：显式等待、隐式等待的区别与应用场景
- 异常处理：如何编写健壮的测试脚本
- JavaScript 执行：在 Selenium 中调用 JS 解决交互问题
- 测试验证：如何有效断言测试结果
## 🔧 故障排除
| 问题现象 | 可能原因 | 解决方案 |
|---------|---------|---------|
| `WebDriverException` | 浏览器驱动版本不匹配 | 下载与浏览器版本一致的驱动 |
| `NoSuchElementException` | 元素定位失败 | 检查元素 ID / 选择器是否正确，增加等待时间 |
| `ElementNotInteractableException` | 元素不可交互 | 使用 `driver.execute_script()` 执行操作 |
| 脚本运行无反应 | Python 路径未配置 | 检查系统环境变量 PATH 配置 |
## 📈 后续计划
- [ ] 添加多关键词数据驱动测试
- [ ] 集成 pytest 测试框架
- [ ] 实现测试报告自动生成
- [ ] 添加失败截图功能
- [ ] 扩展其他网站测试案例

<h1 align='center'>vitesse-lite-py</h1>

<p align='center'>
Mocking up web app with <b>vitesse-lite</b><sup><em>(smaller)</em></sup><br>
</p>

<br>


<br>

<p align='center'>
<b>简体中文</b> | <a href="">English</a>
<!-- Contributors: Thanks for getting interested, however we DON'T accept new transitions to the README, thanks. -->
</p>

<br>

## 介绍

### 👀 `vitesse-lite-py`

- vitesse-lite-py 帮助您构建 windows、macos、linux 平台客户端的应用，不再受pyqt的困扰。
- vitesse-lite-py 的视图层采用 HTML+JS+CSS，业务层采用本地 Python，开发者无需关注前后端连接，只需关注视图效果和业务逻辑本身。
- vitesse-lite-py 采用了 Vite 的开发模式，支持热更新，开发体验更佳。
- vitesse-lite-py 采用了 PyInstaller 打包，打包体积更小。
- vitesse-lite-py 采用了 pywebview 作为渲染引擎，渲染速度更快。
- vitesse-lite-py 采用了 Vue3、Vitesse-lite 作为前端框架，代码编写更优雅从容。
- vitesse-lite-py 采用了 Python 编程语言开发业务层，模块丰富。

### 📦 适用场景

- 对软件的用户界面有一定美感要求
- 需要用到 Python 中的人工智能等模块
- 考虑搭建本地应用，使用本机计算和存储资源
- 对软件功能要求比较高，需要自己开发

### 👨‍💻 适用人群

- 熟悉 Vue3 和 Python 编程的程序员。
- 熟悉 HTML、CSS、JS 的前端工程师。
- 熟悉 Python 的数据分析师。
- 熟悉 Python 的机器学习工程师。
- 熟悉 Python 的人工智能工程师。
- 熟悉 Python 的软件工程师。

### 使用要求

- npm 8.0+
- Python 3.6-3.8

## 特性

- ⚡️ [Vue 3](https://github.com/vuejs/core), [Vite 3](https://github.com/vitejs/vite), [npm](https://npm.io/), [ESBuild](https://github.com/evanw/esbuild) - born with fastness

- 🗂 [File based routing](./src/pages)

- 📦 [Components auto importing](./src/components)

- 🎨 [UnoCSS](https://github.com/antfu/unocss) - The instant on-demand atomic CSS engine.

- 😃 Use icons from any icon sets in [Pure CSS](https://github.com/antfu/unocss/tree/main/packages/preset-icons)

- 🔥 Use the [new `<script setup>` style](https://github.com/vuejs/rfcs/pull/227)

- ✅ Use [Vitest](http://vitest.dev/) for unit and components testing

- 🦾 TypeScript, of course


<br>

## 尝试

```bash

### GitHub Template

[Create a repo from this template on GitHub](https://github.com/MarleneJiang/vitesse-lite-py).

### Clone to local

If you prefer to do it manually with the cleaner git history

```bash
git clone https://github.com/MarleneJiang/vitesse-lite-py.git
cd vitesse-lite-py
npm i
```

## 使用

```
# 开发模式
npm run start

# 开发模式，cef兼容模式【仅win系统】
npm run start:cef

# 预打包，带console，方便输出日志信息
npm run pre

# 预打包，带console，cef兼容模式【仅win系统】
npm run pre:cef

# 预打包，带console，生成文件夹【仅win系统】
npm run pre:folder

# 预打包，带console，生成文件夹，cef兼容模式【仅win系统】
npm run pre:folder:cef


# 正式打包
npm run build

# 正式打包，cef兼容模式【仅win系统】
npm run build:cef

# 正式打包，生成文件夹【仅win系统】
npm run build:folder

# 正式打包，生成文件夹，cef兼容模式【仅win系统】
npm run build:folder:cef
```


## 高级用法

### 客户端引擎介绍

`vitesse-lite-py` 基于 [pywebview](https://pywebview.flowrl.com) 构建客户端。而 pywebview 构架构建客户端的原理是利用本地电脑自带的浏览器引擎驱动，模拟生成客户端。本质上还是网页，或者说是一个浏览器，但是感官上和本地客户端没有差别。

那么，基于 pywebview 构架构建客户端的成败或质量，就与本地电脑的浏览器引擎息息相关了。

#### windows 系统

在 windows 系统上，大体上分为两类客户端引擎：正常模式和兼容模式。

- 正常模式

正常模式下，按照 edgechromium ，edgehtml， mshtml 的客户端引擎依次检索。如果本地电脑 edge 浏览器支持这些引擎，则客户端可以正常启动。否则，请安装对应的 [EdgeWebView2Runtime](https://developer.microsoft.com/en-us/microsoft-edge/webview2/) 浏览器引擎。

- 兼容模式

如果本地电脑 edge 浏览器不支持这些引擎，同时也不想下载 [EdgeWebView2Runtime](https://developer.microsoft.com/en-us/microsoft-edge/webview2/) ，那么就可以使用兼容模式。兼容模式的原理就是利用 [CEFPython](https://github.com/cztomczak/cefpython)，嵌入 Chromium 的 Web 浏览器控件。也就是只要本地电脑安装了谷歌浏览器 V66 版及其以上版本，即可正常启动客户端。缺点就是生成的安装包体积会增加大约 60M 左右。

#### macOS 系统

macOS 系统的浏览器引擎由于 macOS 系统的封闭性，就只有一种 WebKit 引擎可用。

需要注意的是，MacOs在m系列芯片和x86芯片下无法共用同一个安装包，所以需要分别打包。

### 域间通信

#### 从 Python 调用 Javascript

window.evaluate_js(code, callback=None)允许您使用同步返回的最后一个值执行任意 Javascript 代码。如果提供了回调函数，则解析 promise，并调用回调函数，结果作为参数。Javascript 类型转换为 Python 类型，例如 JS 对象到 Python 字典，数组到列表，未定义为 None。由于实现限制，字符串“null”将被计算为 None。另外，evaluate_js 返回的值限制为 900 个字符内。

#### 从 Javascript 调用 Python

从 Javascript 调用 Python 函数可以通过两种不同的方法完成。

- 通过将 Python 类的实例暴露给 create_window 的 js_api。该类的所有可调用方法都将以 pywebview.api.method_name 的形式公开到 JS 域中。方法名称不得以下划线开头。
- 通过将函数传递给窗口对象的 expose(func)这将以 pywebview.api.func_name 的形式将一个或多个函数公开到 JS 域。与 JS API 不同，expose 也允许在运行时公开函数。如果 JS API 和以这种方式公开的函数之间存在名称冲突，则后者优先。

### 热更新

- 使用 npm-run-all 并行启用 vite(自带热更新) 和 pywebview
- 使用 nodemon 监听 `api/*` `core/*` `main.py` 等文件，有修改自动重启应用，达到 HRM 效果

### 注意问题

- 在 windows 系统下，只能打包 exe 等适用于 windows 的程序，不能打包 mac 系统下的 app 程序。同理，mac 也是一样。
- 在 windows 系统下，请不要使用中文路径，否则可能会出现 cannot call null pointer pointer from cdata 'int(_)(void _, int)' 等错误信息。mac 系统无此问题。
- static 静态文件夹，可以存放 cache 缓存、db 数据库等，这些文件都将被直接打包到程序包中


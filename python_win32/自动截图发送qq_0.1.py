import win32con,win32gui,time,win32api

x = 1
while x==1:

	#win32api.keybd_event(0,37,0,0)		按下截图键 用 VK_SNAPSHOT 不行，只好用扫描码，虚拟键值>=1，结果扫描码也不行

	win32api.keybd_event(win32con.VK_SNAPSHOT, 0)	#https://www.cnblogs.com/xieqiankun/p/usePythonForScreenShot.html

	time.sleep(1)


	hwnd = 264644    ### 这里是聊天QQ窗口的句柄  十进制的

	win32gui.ShowWindow(hwnd, 8)    # SW_SHOWNA：以窗口原来的状态显示窗口。激活窗口仍然维持激活状态。nCmdShow=8。
	time.sleep(0.5)

	#鼠标定位到1144,676
	win32api.SetCursorPos([1144,676])
	time.sleep(0.3)

	#执行左单键击，若需要双击则延时几毫秒再点击一次即可
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
	time.sleep(0.3)

	win32gui.PostMessage(hwnd,win32con.WM_PASTE, 0, 0)  # 向窗口发送剪贴板内容
	 
	time.sleep(0.3)
	 
	win32gui.PostMessage(hwnd,win32con.WM_KEYDOWN,win32con.VK_RETURN,0)  #  向窗口发送 回车键  
	 
	win32gui.PostMessage(hwnd,win32con.WM_KEYUP,win32con.VK_RETURN,0)

	time.sleep(1)

	win32gui.PostMessage(hwnd,win32con.WM_KEYDOWN,win32con.VK_ESCAPE,0)  #  向窗口发送 esc键  （虚拟键值表）
	 
	win32gui.PostMessage(hwnd,win32con.WM_KEYUP,win32con.VK_ESCAPE,0)
	
	time.sleep(600)	#每10分钟发一次

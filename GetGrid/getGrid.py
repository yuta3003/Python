import cv2

def main():
    read = cv2.imread("lena.jpg")   # 入力画像
    window_name = "input window"    # 表示するWindow名
    cv2.imshow(window_name, read)   # 画像の表示
    mouseData = mouseParam(window_name) # コールバックの設定
    
    while True:
        cv2.waitKey(20) # ??
        if mouseData.getEvent() == cv2.EVENT_LBUTTONDOWN:   # 左クリック時動作：表示
            print(mouseData.getPos())
        elif mouseData.getEvent() == cv2.EVENT_RBUTTONDOWN: # 右クリック時動作：終了
            break

    cv2.destroyAllWindows() # 画面破棄
    print("Finished")


class mouseParam:
    def __init__(self, input_img_name):
        self.mouseEvent = {"x":None, "y":None, "event":None, "flags":None}  #マウス入力用のパラメータ
        cv2.setMouseCallback(input_img_name, self.__CallBackFunc, None)     #マウス入力の設定
    
    #コールバック関数
    def __CallBackFunc(self, eventType, x, y, flags, userdata):
        
        self.mouseEvent["x"] = x
        self.mouseEvent["y"] = y
        self.mouseEvent["event"] = eventType    
        self.mouseEvent["flags"] = flags    

    #マウス入力用のパラメータを返すための関数
    def getData(self):
        return self.mouseEvent
    
    #マウスイベントを返す関数
    def getEvent(self):
        return self.mouseEvent["event"]                

    #マウスフラグを返す関数
    def getFlags(self):
        return self.mouseEvent["flags"]                

    #xの座標を返す関数
    def getX(self):
        return self.mouseEvent["x"]  

    #yの座標を返す関数
    def getY(self):
        return self.mouseEvent["y"]  

    #xとyの座標を返す関数
    def getPos(self):
        return (self.mouseEvent["x"], self.mouseEvent["y"])
        

if __name__ == '__main__':
    main()
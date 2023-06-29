import math
class Exception:
    def ex1(self, n):
        if n < 2: return False
        check = True
        for i in range(2, int(math.sqrt(n))):
            if n%i == 0:
                return False
        return True
    def ex2(self, n):
        if n < 2: return False
        check = True
        for i in range(2, int(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True
    def ex5(self):
        
        check = True
        n = 0
        # while check:
        try:
            a = float(input())
            b = float(input())
            print(a/b)
        except ZeroDivisionError:
            print("ZeroDivisionError")
        except ValueError:
            print('ValueError')
        except:
            print("Loi Khac")
        else:
            print("Thu nghiem EXC")
    def ex7(self):
        
        check = True
        n = 0
        # while check:
        try:
            a = float(input())
            b = float(input())
            print(a/b)
        except ZeroDivisionError:
            print("ZeroDivisionError")
        except ValueError:
            print('ValueError')
        except:
            print("Loi Khac")
        else:
            print("Thu nghiem EXC")
        finally:
            print("Thu nghiem Finally")
    
    def ex8(self, n):
        
        check = True
        n = 0
        while check:
            try:
               
                check = False 
            except ZeroDivisionError:
                print("ZeroDivisionError")
          
            except ValueError:
                print('ValueError')
       
            except:
                print("Loi Khac")
        
            else:
                print("Thanh cong")
    def ex10(self):
        
        check = True
        n = 0
        while check:
            ls = []
            for i in range(5):
                a = input()
                ls.append(a)
            for i in range(5):
                ls[i] = int(ls[i])
    def KalvinToFahren(self, c):
        assert c>=0, "Nhiet do lon hon 0"
        return 90
        
if __name__=="__main__":
    ex = Exception()
    # ex.ex1(10)
    print(ex.KalvinToFahren(-1))
# mssv
# hv
# ngay sinh
# que __quan
# gio tinh
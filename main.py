from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager, SwapTransition
from kivymd.app import MDApp
from important import Shapes
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.navigationdrawer import MDNavigationLayout
Window.size = (290, 580)
class Navigation_Layout():
    pass
def snackbarforinput():
    Snackbar(text="[color=#ff6961]Please fill the all the required blanks[/color]",).open()
def snackbar_for_pie():
    Snackbar(text="[color=#ff6961]Please select value of pi[/color]",).open()
class MainScreen(Screen):
    class MyNavigationLayout(MDNavigationLayout):
        class Navigation_ScreenManager(ScreenManager):
            class Screen_about(Screen):
                def load_table(self):
                    layout = BoxLayout()
                    self.data_table = MDDataTable(pos_hint={"center_x":0.5, "center_y":0.5},
                            size_hint=(0.975,0.95),
                            rows_num = 22,
                            column_data=[
                                ("Name", dp(30)),
                                ("From", dp(20)),
                                ("Helped in..", dp(75))
                            ],
                            row_data=[
                                ("Jagadeeshwar", "School", "Icon"),
                                ("Dart", "Discord-KivyMD", "MDDataTable, Buildozer, GridLayout, Bugs, IconLeftWidgetWithoutTouch"),
                                ("neon jadd", "Discord-KivyMD", "MDDataTable, GridLayout, MDList, Performance, NavigationDrawer"),
                                ("Yuri Ivanov", "Discord-KivyMD", "Bug, IconLeftWidgetWithoutTouch"),
                                ("darpan5552", "Discord-KivyMD", "InnerIcons"),
                                ("zdayX", "Discord-KivyMD", "InnerApp"),
                                ("RobertFlatt", "Discord-Kivy", "Kivy"),
                                ("VICTOR D.VICIKIE", "Discord-Kivy", "Kivy-size_hint"),
                                ("tshirtman", "Discord-Kivy", "Kivy"),
                                ("Stackoverflow", "Websites", "It's everything"),
                                ("GeeksforGeeks", "Websites", "It helped a lot")
                            ]
                            )
                    self.add_widget(self.data_table)
                    return layout
                def on_enter(self):
                    self.load_table()
            class Screen_formulas_3d(Screen):
                def load_table(self):
                    layout = BoxLayout()
                    self.data_table = MDDataTable(pos_hint={"center_x":0.5, "center_y":0.5},
                            size_hint=(0.975,0.95),
                            check = True,
                            rows_num = 22,
                            column_data=[
                                ("No.", dp(20)),
                                ("Shapes", dp(30)),
                                ("Volume", dp(50)),
                                ("T.S.A", dp(75)),
                                ("L.S.A/C.S.A", dp(75)),
                                ("Area of Base", dp(30)),
                                ("Area of Face", dp(50)),
                                ("Diagonal/Diameter", dp(30)),
                                ("Height/Slant Height", dp(30)),
                                ("Circumference", dp(30))
                            ],
                            row_data=[
                                ("1.", "Cube", "edge**3", "6*(edge*edge)", "4*(edge*edge)", "---", "---", "(3**(1/2))*edge", "---", "---"),
                                ("2.", "Cuboid", "lenght*breadth*height", "2*((lenght*breadth)+(breadth*height)+(lenght*height))", "---", "---", "---", "((lenght*lenght)+(breadth*breadth)+(height*height))**(1/2)", "---", "---"),
                                ("3.", "Triangular Prism", "ar_base*height", "(2*ar_base)+((side1+side2+side3)*height)", "(side1+side2+side3)*height", "((s*(s-side1)*(s-side2)*(s-side3))**(1/2))", "---", "---", "---", "---"),
                                ("4.", "Triangular Pyramid", "(1/3)*ar_base*height", "ar_base+((1/2)*(pr_base*sl_height))", "(1/2)*(pr_base*sl_height)", "---", "---", "---", "---", "---"),
                                ("5.", "Square Pyramid", "(side*side)*(height/3)", "(side*side)+(2*side)*(((side*side)/4)+(height*height))**(1/2)", "side*((side*side)+4*(height*height))**(1/2)", "side*side", "(side/2)*(((side*side)/4)+(height*height))**(1/2)", "---", "---", "---"),
                                ("6.", "Rectanglular Pyramid", "(lenght*breadth*height)/3", "(lenght*breadth)+lenght*((((breadth/2)**2)+(height*height))**(1/2))+breadth*((((lenght/2)**2)+(height*height))**(1/2))", "lenght*((((breadth/2)**(2))+(height*height))**(1/2))+breadth*((((lenght/2)**(2))+(height*height))**(1/2))", "lenght*breadth", "---", "---", "---", "---"),
                                ("7.", "Pentagonal Pyramid", "(5/12)*tan(54)*height*(side*side) #1.376", "(5/4)*tan(54)*(side*side)+(5*(side/2))*((height*height)+(((side*tan(54))/2)**2))**(1/2)", "(5*side*((height*height)+(((side*tan(54))/2)**2))**(1/2))/2", "(5/4)*tan(54)*side*side #1.376", "(side/2)*((height*height)+(((side*side)/2)**2))**(1/2)", "---", "---", "---"),
                                ("8.", "Hexagonal Pyramid", "((3**(1/2))/2)*(side*side)*height", "((3*(3**(1/2)))/2)*(side*side)+(3*side)*((height*height)+((3*side*side)/4))**(1/2)", "(3*side)*((height*height)+((3*side*side)/4))**(1/2)", "((3*(3**(1/2)))/2)*(side*side)", "(side/2)*((height*height)+((3*side*side)/4))**(1/2)", "---", "---", "---"),
                                ("9.", "Tetrahedron", "(side*side*side)/(6*(2**(1/2)))", "(3**(1/2))*side*side", "---", "---", "((3**(1/2))/4)*side*side", "---", "((2/3)**(1/2))*side", "---"),
                                ("10.", "Octahedron", "((2**(1/2))/3)*(side**3)", "2*(3**(1/2))*side*side", "---", "---", "---", "---", "---", "---"),
                                ("11.", "Dodecahedron", "((15+7*(5**(1/2)))/4)*(side*side*side)", "3*((25+10*((5**(1/2))))**(1/2))*side*side", "---", "---", "---", "---", "---", "---"),
                                ("12.", "Icosahedron", "((5*(3+(5**(1/2))))/12)*(side*side*side)", "5*(3**(1/2))*(side*side)", "---", "---", "---", "---", "---", "---"),
                                ("13.", "Sphere", "(4/3)*(pie)*(radius*radius*radius)", "4*(pie)*(radius*radius)", "---", "---", "---", "2*radius", "---", "2*(pie)*radius"),
                                ("14.", "Hemi-Sphere", "(2/3)*(pie)*(radius*radius*radius)", "3*(pie)*(radius*radius)", "2*(pie)*radius*radius", "(pie)*radius*radius", "---", "2*radius", "---", "2*(pie)*radius"),
                                ("15.", "Ellipsoid", "(4/3)*(pie)*x*y*z", "4*(pie)*((((x*y)**(1.6))+((x*z)**(1.6))+((y*z)**(1.6)))/3)**(1/1.6)", "---", "---", "---", "---", "---", "---"),
                                ("16.", "Cylinder", "(pie)*radius*radius*height", "(2*(pie)*radius*height)+(2*(pie)*radius*radius)", "2*(pie)*radius*height", "(pie)*radius*height", "---", "2*radius", "---", "---"),
                                ("17.", "Cone", "(pie)*radius*radius*(height/3)", "(pie)*radius*(radius+((height*height)+(radius*radius))**(1/2))", "(pie)*radius*(((height*height)+(radius*radius))**(1/2))", "(pie)*radius*radius", "---", "2*radius", "((radius*radius)+(height*height))**(1/2)", "---"),
                                ("18.", "Torus", "2*((pie)**2)*radius1*((radius2)**2)", "4*((pie)**2)*radius1*radius2", "---", "---", "---", "---", "---", "---")
                            ]
                            )
                    self.add_widget(self.data_table)
                    return layout
                def on_enter(self):
                    self.load_table()
                            
            class Screen_formulas_2d(Screen):
                def load_table(self):
                    layout = BoxLayout()
                    self.data_table = MDDataTable(pos_hint={"center_x":0.5, "center_y":0.5},
                                            size_hint=(0.975,0.95),
                                            check = True,
                                            rows_num = 22,
                                            column_data=[
                                                ("No.", dp(20)),
                                                ("Shapes", dp(30)),
                                                ("Area", dp(50)),
                                                ("Perimeter", dp(30)),
                                                ("Diagonal/Diameter", dp(30)),
                                                ("Side", dp(30)),
                                                ("Hypotenuse/Height", dp(30))
                                            ],
                                            row_data=[
                                                ("1.", "Triangle", "(1/2)*base*height", "---", "---", "---", "---"),
                                                ("2.", "Equilateral Triangle", "((3**(1/2))/4)*side*side", "3*side", "---", "---", "---"),
                                                ("3.", "Right Triangle", "(side1*side2)/2", "side1+side2+hypotenuse", "---", "---", "((side1*side1)+(side2*side2))**(1/2)"),
                                                ("4.", "Isosceles Triangle", "(side/2)*((side*side)-(common*common))**(1/2)", "(2*common)+side", "---", "---", "2*(area/side)"),
                                                ("5.", "Scalene Triangle", "(s*(s-side1)*(s-side2)*(s-side3))**(1/2)", "s*2", "---", "---", "---"),
                                                ("6.", "Quadrilateral", "((1/2*diagnol*dia1)+(1/2*diagnol*dia2))", "---", "---", "---", "---"),
                                                ("7.", "Square", "side*side", "4*side", "---", "---", "---"),
                                                ("8.", "Rectangle", "lenght*width", "2*(lenght+width)", "---", "---", "---"),
                                                ("9.", "Rhombus", "(dia1*dia2)/2", "2*((dia1*dia1)+(dia2*dia2))**(1/2)", "---", "(((dia1/2)*(dia1/2))+((dia2/2)*(dia2/2)))**(1/2)", "---"),
                                                ("10.", "Kite", "(dia1*dia2)/2", "2*(side1+side2)", "---", "---", "---"),
                                                ("11.", "Parallelogram", "base*height", "2*(side+base)", "---", "---", "---"),
                                                ("12.", "Trapezium", "(1/2)*(par1+par2)*height", "par1+par2+side1+side2", "---", "---", "---"),
                                                ("13.", "Regular Pentagon", "(1/4)*((5*(5+2*(5**(1/2))))**(1/2))*(side*side)", "5*side", "((1+(5**(1/2)))/2)*side", "---", "---"),
                                                ("14.", "Regular Hexagon", "((3*(3**(1/2)))/2)*(side*side)", "6*side", "---", "---", "---"),
                                                ("15.", "Regular Heptagon", "(7/4)*(side*side)*cot(180/7) #2.0765", "7*side", "---", "---", "---"),
                                                ("16.", "Regular Octagon", "2*(1+(2**(1/2)))*(side*side)", "8*side", "---", "---", "---"),
                                                ("17.", "Regular Nonagon", "(9/4)*(side*side)*cot(180/9) #2.747", "9*side", "---", "---", "---"),
                                                ("18.", "Regular Decagon", "(5/2)*(side*side)*(5+2*(5**(1/2)))**(1/2)", "10*side", "---", "---", "---"),
                                                ("19.", "Circle", "(pie)*radius*radius", "2*(pie)*radius", "2*radius", "---", "---"),
                                                ("20.", "Semi-Circle", "(1/2)*((pie)*(radius*radius))", "((pie)*radius)+(2*radius)", "2*radius", "---", "---"),
                                                ("21.", "Ellipse", "(pie)*x*y", "(pie)*(3*(x+y)-(((3*x+y)*(x+3*y))**(1/2)))", "---", "---", "---")
                                            ]
                                            )
                    self.add_widget(self.data_table)
                    return layout
                def on_enter(self):
                    self.load_table()


class TriangleWindow(Screen):
    def queans(self):
        base_input = self.ids.base_value.text
        height_input = self.ids.height_value.text
        try:
            base_input = float(base_input)
            height_input = float(height_input)
        except ValueError:
            snackbarforinput()
        if base_input != '' and height_input != '':
            answer = Shapes.triangle(base_input, height_input)
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
        
class EquilateralTriangleWindow(Screen):
    def queans(self):
        base_input = self.ids.base_value.text
        try:
            base_input = float(base_input) #  #FF3030 #ddbb34 #ff6961
        except ValueError:
            snackbarforinput()
        if base_input != '':
            answer = Shapes.equilateral_triangle(float(base_input))
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
        
class RightTriangleWindow(Screen):
    def queans(self):
        side1_input = self.ids.side1_value.text
        side2_input = self.ids.side2_value.text
        try:
            side1_input = float(side1_input)
            side2_input = float(side2_input)
        except ValueError:
            snackbarforinput()
        if side1_input != '' and side2_input != '':
            answer = Shapes.right_triangle(float(side1_input), float(side2_input))
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
            self.ids.hypotenuse_value.hint_text = str(answer[2])

class IsoscelesTriangleWindow(Screen):
    def queans(self):
        base_input = self.ids.base_value.text
        height_input = self.ids.height_value.text
        try:
            base_input = float(base_input)
            height_input = float(height_input)
        except ValueError:
            snackbarforinput()
        if base_input != '' and height_input != '':
            answer = Shapes.iso_triangle(float(base_input), float(height_input))
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
            self.ids.side_value.hint_text = str(answer[2])
        
class ScaleneTriangleWindow(Screen):
    def queans(self):
        side1_input = self.ids.side1_value.text
        side2_input = self.ids.side2_value.text
        side3_input = self.ids.side3_value.text
        try: 
            side1_input = float(side1_input)
            side2_input = float(side2_input)
            side3_input = float(side3_input)
        except ValueError:
            snackbarforinput()
        if side1_input != '' and side2_input != '' and side3_input != '':
            answer = Shapes.scal_triangle(float(side1_input), float(side2_input), float(side3_input))
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
            
class QuadrilateralWindow(Screen):
    def queans(self):
        large_dia_input = self.ids.large_dia_value.text
        small_dia_1_input = self.ids.small_dia_1_value.text
        small_dia_2_input = self.ids.small_dia_2_value.text
        try:
            large_dia_input = float(large_dia_input)
            small_dia_1_input = float(small_dia_1_input)
            small_dia_2_input = float(small_dia_2_input)
        except ValueError:
            snackbarforinput()    
        if large_dia_input != '' and small_dia_1_input != '' and small_dia_2_input != '':
            answer = Shapes.quad(large_dia_input, small_dia_1_input, small_dia_2_input)
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
            
class RectangleWindow(Screen):
    def queans(self):
        lenght_input = self.ids.lenght_value.text
        width_input = self.ids.width_value.text
        try: 
            lenght_input = float(lenght_input)
            width_input = float(width_input)
        except ValueError:
            snackbarforinput()
        if lenght_input != '' and width_input != '':
            answer = Shapes.rectangle(lenght_input, width_input)
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
            self.ids.diagonal_value.hint_text = str(answer[2])
        
class SquareWindow(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        try: 
            side_input = float(side_input)
        except ValueError:
            snackbarforinput()
        if side_input != '':
            answer = Shapes.square(side_input)
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
            
class RhombusWindow(Screen):
    def queans(self):
        dia_1_input = self.ids.dia_1_value.text
        dia_2_input = self.ids.dia_2_value.text
        try: 
            dia_1_input = float(dia_1_input)
            dia_2_input = float(dia_2_input)
        except ValueError:
            snackbarforinput()
        if dia_1_input != '' and dia_2_input != '':
            answer = Shapes.rhombus(dia_1_input, dia_2_input)
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
            self.ids.side_value.hint_text = str(answer[2])
            
class KiteWindow(Screen):
    def queans(self):
        dia_1_input = self.ids.dia_1_value.text
        dia_2_input = self.ids.dia_2_value.text
        side_1_input = self.ids.side_1_value.text
        side_2_input = self.ids.side_2_value.text
        try: 
            dia_1_input = float(dia_1_input)
            dia_2_input = float(dia_2_input)
            side_1_input = float(side_1_input)
            side_2_input = float(side_2_input)
        except ValueError:
            snackbarforinput()
        if dia_1_input != '' and dia_2_input != '' and side_1_input != '' and side_2_input != '':
            answer = Shapes.kite(dia_1_input, dia_2_input, side_1_input , side_2_input)
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
    
class ParallelogramWindow(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        base_input = self.ids.base_value.text
        height_input = self.ids.height_value.text
        try: 
            side_input = float(side_input)
            base_input = float(base_input)
            height_input = float(height_input)
        except ValueError:
            snackbarforinput()
        if side_input != '' and base_input != '' and height_input != '':
            answer = Shapes.par_gm(side_input, base_input, height_input)
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
    
class TrapeziumWindow(Screen):
    def queans(self):
        par_1_input = self.ids.par_1_value.text
        par_2_input = self.ids.par_2_value.text
        height_input = self.ids.height_value.text
        side_1_input = self.ids.side_1_value.text
        side_2_input = self.ids.side_2_value.text
        try: 
            par_1_input = float(par_1_input)
            par_2_input = float(par_2_input)
            height_input = float(height_input)
            side_1_input = float(side_1_input)
            side_2_input = float(side_2_input)
        except ValueError:
            snackbarforinput()
        if par_1_input != '' and par_2_input != '' and height_input !='' and side_1_input != '' and side_2_input != '':
            answer = Shapes.trap(par_1_input, par_2_input, height_input, side_1_input , side_2_input)
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
    
class RegularPentagonWindow(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        try: 
            side_input = float(side_input)
        except ValueError:
            snackbarforinput()
        if side_input != '':
            answer = Shapes.reg_pent(side_input)
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
            self.ids.diagonal_value.hint_text = str(answer[2])
    
class RegularHexagonWindow(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        try: 
            side_input = float(side_input)
        except ValueError:
            snackbarforinput()
        if side_input != '':
            answer = Shapes.reg_hex(side_input)
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
    
class RegularHeptagonWindow(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        try: 
            side_input = float(side_input)
        except ValueError:
            snackbarforinput()
        if side_input != '':
            answer = Shapes.reg_hept(side_input)
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])

class RegularOctagonWindow(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        try: 
            side_input = float(side_input)
        except ValueError:
            snackbarforinput()
        if side_input != '':
            answer = Shapes.reg_oct(side_input)
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
    
class RegularNonagonWindow(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        try: 
            side_input = float(side_input)
        except ValueError:
            snackbarforinput()
        if side_input != '':
            answer = Shapes.reg_nona(side_input)
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
    
class RegularDecagonWindow(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        try: 
            side_input = float(side_input)
        except ValueError:
            snackbarforinput()
        if side_input != '':
            answer = Shapes.reg_deca(side_input)
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
    
class CircleWindow(Screen):
    def pi(smt,pi_value):
        global pi_for_cir
        hival = pi_value
        pi_for_cir = hival
    def queans(self):
        radius_input = self.ids.radius_value.text
        try: 
            radius_input = float(radius_input)
        except ValueError:
            snackbarforinput()
        if radius_input != '':
            try:
                if pi_for_cir == "22/7":
                    answer = Shapes.cir_acc(radius_input)
                    self.ids.area_value.hint_text = str(answer[0])
                    self.ids.perimeter_value.hint_text = str(answer[1])
                elif pi_for_cir == "3.141":
                    answer = Shapes.cir_exc(radius_input)
                    self.ids.area_value.hint_text = str(answer[0])
                    self.ids.perimeter_value.hint_text = str(answer[1])
                else:
                    snackbar_for_pie()
            except NameError:
                snackbar_for_pie()
    
class SemiCircleWindow(Screen):
    def pi(smt,pi_value):
        global pi_for_sm_cir
        hival = pi_value
        pi_for_sm_cir = hival
    def queans(self):
        radius_input = self.ids.radius_value.text
        try: 
            radius_input = float(radius_input)
        except ValueError:
            snackbarforinput()
        if radius_input != '':
            try:
                if pi_for_sm_cir == "22/7":
                    answer = Shapes.sm_cir_acc(radius_input)
                    self.ids.area_value.hint_text = str(answer[0])
                    self.ids.perimeter_value.hint_text = str(answer[1])
                elif pi_for_sm_cir == "3.141":
                    answer = Shapes.sm_cir_exc(radius_input)
                    self.ids.area_value.hint_text = str(answer[0])
                    self.ids.perimeter_value.hint_text = str(answer[1])
                else:
                    snackbar_for_pie()
            except NameError:
                snackbar_for_pie()
    
class EllipseWindow(Screen):
    def pi(smt,pi_value):
        global pi_for_ellipse
        hival = pi_value
        pi_for_ellipse = hival
    def queans(self):
        x_input = self.ids.x_value.text
        y_input = self.ids.y_value.text
        try: 
            x_input = float(x_input)
            y_input = float(y_input)
        except ValueError:
            snackbarforinput()
        if x_input != '' and y_input != '':
            try:
                if pi_for_ellipse == "22/7":
                    answer = Shapes.ell_acc(x_input, y_input)
                    self.ids.area_value.hint_text = str(answer[0])
                    self.ids.circumference_value.hint_text = str(answer[1])
                elif pi_for_ellipse == "3.141":
                    answer = Shapes.ell_exc(x_input, y_input)
                    self.ids.area_value.hint_text = str(answer[0])
                    self.ids.circumference_value.hint_text = str(answer[1])
                else:
                    snackbar_for_pie()
            except NameError:
                snackbar_for_pie()
    
class CubeWindow(Screen):
    def queans(self):
        edge_input = self.ids.edge_value.text
        try: 
            edge_input = float(edge_input)
        except ValueError:
            snackbarforinput()
        if edge_input != '':
            answer = Shapes.cube(edge_input)
            self.ids.volume_value.hint_text = str(answer[0])
            self.ids.tsa_value.hint_text = str(answer[1])
            self.ids.lsa_value.hint_text = str(answer[2])
            self.ids.diagonal_value.hint_text = str(answer[3])
            
class CuboidWindow(Screen):
    def queans(self):
        length_input = self.ids.length_value.text
        breadth_input = self.ids.breath_value.text
        height_input = self.ids.height_value.text
        try: 
            length_input = float(length_input)
            breadth_input = float(breadth_input)
            height_input = float(height_input)
        except ValueError:
            snackbarforinput()
        if length_input != '' and breadth_input != '' and height_input != '':
            answer = Shapes.cuboid(length_input, breadth_input, height_input)
            self.ids.volume_value.hint_text = str(answer[0])
            self.ids.tsa_value.hint_text = str(answer[1])
            self.ids.diagonal_value.hint_text = str(answer[2])
            
class TriangularPrismWindow(Screen):
    def queans(self):
        side_1_input = self.ids.side_1_value.text
        side_2_input = self.ids.side_2_value.text
        side_3_input = self.ids.side_3_value.text
        height_input = self.ids.height_value.text
        try: 
            side_1_input = float(side_1_input)
            side_2_input = float(side_2_input)
            side_3_input = float(side_3_input)
            height_input = float(height_input)
        except ValueError:
            snackbarforinput()
        if side_1_input != '' and side_2_input != '' and side_3_input !='' and height_input != '':
            answer = Shapes.tri_prism(side_1_input, side_2_input, side_3_input, height_input)
            self.ids.volume_value.hint_text = str(answer[0])
            self.ids.tsa_value.hint_text = str(answer[1])
            self.ids.lsa_value.hint_text = str(answer[2])
            self.ids.ar_base_value.hint_text = str(answer[3])
            
class TriangularPyramidWindow(Screen):
    def queans(self):
        ar_base_input = self.ids.ar_base_value.text
        pr_base_input = self.ids.pr_base_value.text
        sl_height_input = self.ids.sl_height_value.text
        height_input = self.ids.height_value.text
        try: 
            ar_base_input = float(ar_base_input)
            pr_base_input = float(pr_base_input)
            sl_height_input = float(sl_height_input)
            height_input = float(height_input)
        except ValueError:
            snackbarforinput()
        if ar_base_input != '' and pr_base_input != '' and sl_height_input !='' and height_input != '':
            answer = Shapes.tri_pyramid(ar_base_input, pr_base_input, sl_height_input, height_input)
            self.ids.volume_value.hint_text = str(answer[0])
            self.ids.tsa_value.hint_text = str(answer[1])
            self.ids.lsa_value.hint_text = str(answer[2])
            
class SquarePyramidWindow(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        height_input = self.ids.height_value.text
        try: 
            side_input = float(side_input)
            height_input = float(height_input)
        except ValueError:
            snackbarforinput()
        if side_input != '' and height_input != '':
            answer = Shapes.sq_pyramid(side_input, height_input)
            self.ids.volume_value.hint_text = str(answer[0])
            self.ids.tsa_value.hint_text = str(answer[1])
            self.ids.lsa_value.hint_text = str(answer[2])
            self.ids.ar_base_value.hint_text = str(answer[3])
            self.ids.ar_face_value.hint_text = str(answer[4])
            
class RectanglePyramidWindow(Screen):
    def queans(self):
        length_input = self.ids.length_value.text
        breadth_input = self.ids.breath_value.text
        height_input = self.ids.height_value.text
        try: 
            length_input = float(length_input)
            breadth_input = float(breadth_input)
            height_input = float(height_input)
        except ValueError:
            snackbarforinput()
        if length_input != '' and breadth_input != '' and height_input != '':
            answer = Shapes.rect_pyramid(length_input, breadth_input, height_input)
            self.ids.volume_value.hint_text = str(answer[0])
            self.ids.tsa_value.hint_text = str(answer[1])
            self.ids.lsa_value.hint_text = str(answer[2])
            self.ids.ar_base_value.hint_text = str(answer[3])
            
class PentagonalPyramidWindow(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        height_input = self.ids.height_value.text
        try: 
            side_input = float(side_input)
            height_input = float(height_input)
        except ValueError:
            snackbarforinput()
        if side_input != '' and height_input != '':
            answer = Shapes.pentagon_pyramid(side_input, height_input)
            self.ids.volume_value.hint_text = str(answer[0])
            self.ids.tsa_value.hint_text = str(answer[1])
            self.ids.lsa_value.hint_text = str(answer[2])
            self.ids.ar_base_value.hint_text = str(answer[3])
            self.ids.ar_face_value.hint_text = str(answer[4])
            
class HexagonalPyramidWindow(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        height_input = self.ids.height_value.text
        try: 
            side_input = float(side_input)
            height_input = float(height_input)
        except ValueError:
            snackbarforinput()
        if side_input != '' and height_input != '':
            answer = Shapes.hexagon_pyramid(side_input, height_input)
            self.ids.volume_value.hint_text = str(answer[0])
            self.ids.tsa_value.hint_text = str(answer[1])
            self.ids.lsa_value.hint_text = str(answer[2])
            self.ids.ar_base_value.hint_text = str(answer[3])
            self.ids.ar_face_value.hint_text = str(answer[4])
            
class TetrahedronWindow(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        try: 
            side_input = float(side_input)
        except ValueError:
            snackbarforinput()
        if side_input != '':
            answer = Shapes.tetra_hedron(side_input)
            self.ids.volume_value.hint_text = str(answer[0])
            self.ids.tsa_value.hint_text = str(answer[1])
            self.ids.ar_face_value.hint_text = str(answer[2])
            self.ids.height_value.hint_text = str(answer[3])
            
class OctahedronWindow(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        try: 
            side_input = float(side_input)
        except ValueError:
            snackbarforinput()
        if side_input != '':
            answer = Shapes.octa_hedron(side_input)
            self.ids.volume_value.hint_text = str(answer[0])
            self.ids.tsa_value.hint_text = str(answer[1])
            
class DodecahedronWindow(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        try: 
            side_input = float(side_input)
        except ValueError:
            snackbarforinput()
        if side_input != '':
            answer = Shapes.dodeca_hedron(side_input)
            self.ids.volume_value.hint_text = str(answer[0])
            self.ids.tsa_value.hint_text = str(answer[1])
            
class IcosahedronWindow(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        try: 
            side_input = float(side_input)
        except ValueError:
            snackbarforinput()
        if side_input != '':
            answer = Shapes.icosa_hedron(side_input)
            self.ids.volume_value.hint_text = str(answer[0])
            self.ids.tsa_value.hint_text = str(answer[1])
            
class SphereWindow(Screen):
    def pi(smt,pi_value):
        global pi_for_sph
        hival = pi_value
        pi_for_sph = hival
    def queans(self):
        radius_input = self.ids.radius_value.text
        try: 
            radius_input = float(radius_input)
        except ValueError:
            snackbarforinput()
        if radius_input != '':
            try:
                if pi_for_sph == "22/7":
                    answer = Shapes.sphere_acc(radius_input)
                    self.ids.volume_value.hint_text = str(answer[0])
                    self.ids.tsa_value.hint_text = str(answer[1])
                    self.ids.circumference_value.hint_text = str(answer[2])
                    self.ids.diameter_value.hint_text = str(answer[3])
                elif pi_for_sph == "3.141":
                    answer = Shapes.sphere_exc(radius_input)
                    self.ids.volume_value.hint_text = str(answer[0])
                    self.ids.tsa_value.hint_text = str(answer[1])
                    self.ids.circumference_value.hint_text = str(answer[2])
                    self.ids.diameter_value.hint_text = str(answer[3])
                else:
                    snackbar_for_pie()
            except NameError:
                snackbar_for_pie()
    
class HemiSphereWindow(Screen):
    def pi(smt,pi_value):
        global pi_for_hm_sph
        hival = pi_value
        pi_for_hm_sph = hival
    def queans(self):
        radius_input = self.ids.radius_value.text
        try: 
            radius_input = float(radius_input)
        except ValueError:
            snackbarforinput()
        if radius_input != '':
            try:
                if pi_for_hm_sph == "22/7":
                    answer = Shapes.hemi_sphere_acc(radius_input)
                    self.ids.volume_value.hint_text = str(answer[0])
                    self.ids.tsa_value.hint_text = str(answer[1])
                    self.ids.csa_value.hint_text = str(answer[2])
                    self.ids.ar_base_value.hint_text = str(answer[3])
                    self.ids.circumference_value.hint_text = str(answer[4])
                    self.ids.diameter_value.hint_text = str(answer[5])
                elif pi_for_hm_sph == "3.141":
                    answer = Shapes.hemi_sphere_exc(radius_input)
                    self.ids.volume_value.hint_text = str(answer[0])
                    self.ids.tsa_value.hint_text = str(answer[1])
                    self.ids.csa_value.hint_text = str(answer[2])
                    self.ids.ar_base_value.hint_text = str(answer[3])
                    self.ids.circumference_value.hint_text = str(answer[4])
                    self.ids.diameter_value.hint_text = str(answer[5])
                else:
                    snackbar_for_pie()
            except NameError:
                snackbar_for_pie()
    
class EllipsoidWindow(Screen):
    def pi(smt,pi_value):
        global pi_for_ellipsoid
        hival = pi_value
        pi_for_ellipsoid = hival
    def queans(self):
        x_input = self.ids.x_value.text
        y_input = self.ids.y_value.text
        z_input = self.ids.z_value.text
        try: 
            x_input = float(x_input)
            y_input = float(y_input)
            z_input = float(z_input)
        except ValueError:
            snackbarforinput()
        if x_input != '' and y_input != '' and z_input != '':
            try:
                if pi_for_ellipsoid == "22/7":
                    answer = Shapes.ellipsoid_acc(x_input, y_input, z_input)
                    self.ids.volume_value.hint_text = str(answer[0])
                    self.ids.tsa_value.hint_text = str(answer[1])
                elif pi_for_ellipsoid == "3.141":
                    answer = Shapes.ellipsoid_exc(x_input, y_input, z_input)
                    self.ids.volume_value.hint_text = str(answer[0])
                    self.ids.tsa_value.hint_text = str(answer[1])
                else:
                    snackbar_for_pie()
            except NameError:
                snackbar_for_pie()
            
class CylinderWindow(Screen):
    def pi(smt,pi_value):
        global pi_for_cill
        hival = pi_value
        pi_for_cill = hival
    def queans(self):
        radius_input = self.ids.radius_value.text
        height_input = self.ids.height_value.text
        try: 
            radius_input = float(radius_input)
            height_input = float(height_input)
        except ValueError:
            snackbarforinput()
        if radius_input != '' and height_input != '' :
            try:
                if pi_for_cill == "22/7":
                    answer = Shapes.cylinder_acc(radius_input, height_input)
                    self.ids.volume_value.hint_text = str(answer[0])
                    self.ids.tsa_value.hint_text = str(answer[1])
                    self.ids.csa_value.hint_text = str(answer[2])
                    self.ids.ar_base_value.hint_text = str(answer[3])
                    self.ids.diameter_value.hint_text = str(answer[4])
                elif pi_for_cill == "3.141":
                    answer = Shapes.cylinder_exc(radius_input, height_input)
                    self.ids.volume_value.hint_text = str(answer[0])
                    self.ids.tsa_value.hint_text = str(answer[1])
                    self.ids.csa_value.hint_text = str(answer[2])
                    self.ids.ar_base_value.hint_text = str(answer[3])
                    self.ids.diameter_value.hint_text = str(answer[4])
                else:
                    snackbar_for_pie()
            except NameError:
                snackbar_for_pie()
            
class ConeWindow(Screen):
    def pi(smt,pi_value):
        global pi_for_cone
        hival = pi_value
        pi_for_cone = hival
    def queans(self):
        radius_input = self.ids.radius_value.text
        height_input = self.ids.height_value.text
        try: 
            radius_input = float(radius_input)
            height_input = float(height_input)
        except ValueError:
            snackbarforinput()
        if radius_input != '' and height_input != '' :
            try:
                if pi_for_cone == "22/7":
                    answer = Shapes.cone_acc(radius_input, height_input)
                    self.ids.volume_value.hint_text = str(answer[0])
                    self.ids.tsa_value.hint_text = str(answer[1])
                    self.ids.csa_value.hint_text = str(answer[2])
                    self.ids.ar_base_value.hint_text = str(answer[3])
                    self.ids.slant_height_value.hint_text = str(answer[4])
                    self.ids.diameter_value.hint_text = str(answer[5])
                elif pi_for_cone == "3.141":
                    answer = Shapes.cone_exc(radius_input, height_input)
                    self.ids.volume_value.hint_text = str(answer[0])
                    self.ids.tsa_value.hint_text = str(answer[1])
                    self.ids.csa_value.hint_text = str(answer[2])
                    self.ids.ar_base_value.hint_text = str(answer[3])
                    self.ids.slant_height_value.hint_text = str(answer[4])
                    self.ids.diameter_value.hint_text = str(answer[5])
                else:
                    snackbar_for_pie()
            except NameError:
                snackbar_for_pie()
            
class TorusWindow(Screen):
    def pi(smt,pi_value):
        global pi_for_tor
        hival = pi_value
        pi_for_tor = hival
    def queans(self):
        radius_1_input = self.ids.radius_1_value.text
        radius_2_input = self.ids.radius_2_value.text
        try: 
            radius_1_input = float(radius_1_input)
            radius_2_input = float(radius_2_input)
        except ValueError:
            snackbarforinput()
        if radius_1_input != '' and radius_2_input!= '':
            try:
                if pi_for_tor == "22/7":
                    answer = Shapes.torus_acc(radius_1_input, radius_2_input)
                    self.ids.volume_value.hint_text = str(answer[0])
                    self.ids.tsa_value.hint_text = str(answer[1])
                elif pi_for_tor == "3.141":
                    answer = Shapes.torus_exc(radius_1_input, radius_2_input)
                    self.ids.volume_value.hint_text = str(answer[0])
                    self.ids.tsa_value.hint_text = str(answer[1])
                else:
                    snackbar_for_pie()
            except NameError:
                snackbar_for_pie()

class MyScreenManager(ScreenManager):
    def change_screen_for_shapes(self, screen):
        self.current = screen  # the same as in .kv: app.root.current = screen
        self.transition.direction= "right"
        #self.transition = SwapTransition()

class TestApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'DeepPurple'
        self.theme_cls.primary_hue = '50'   ##Pentagrammic prism
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.accent_palette = 'Blue'
        self.icon = 'iconforapp.png'


TestApp().run()

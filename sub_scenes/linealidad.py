from manim import config, WHITE, Text, BLUE, UP, BLACK, VGroup, RIGHT, DOWN, LEFT, DL, GRAY, DR, MathTex, GREEN, RED, Write, FocusOn, TransformMatchingTex, LaggedStart, AnimationGroup, ReplacementTransform, FadeOut, FadeIn, SVGMobject
from manim_voiceover import VoiceoverScene

config.background_color = WHITE
Text.set_default(color=BLACK)
MathTex.set_default(color=BLACK)

class Linealidad(VoiceoverScene):
    def setup(main_scene):
        from manim_voiceover.services.gtts import GTTSService
        from manim_voiceover.services.recorder import RecorderService

        #main_scene.set_speech_service(RecorderService())
        main_scene.set_speech_service(GTTSService("es", transcription_model='base'))

        main_scene.title = Text("Clasificación", font_size=80, color=BLUE).to_edge(UP)
        main_scene.tipos = VGroup(Text("Tipo"), Text("Orden"), Text("Linealidad")).arrange_submobjects(RIGHT, buff=1.5).next_to(main_scene.title, DOWN).shift(0.5*DOWN+RIGHT)
        main_scene.center = main_scene.tipos[0].get_center()
        main_scene.center_1 = main_scene.tipos[1].get_center()
        main_scene.tipos[0].move_to(main_scene.title.get_center()).scale(1.75)
        edo = Text("EDO", font_size=45).next_to(main_scene.tipos[0], DL).shift(LEFT)
        edo_expanded = Text("Ecuación Diferencial Ordinaria", font_size=25, color=GRAY).next_to(edo, DOWN)
        edp = Text("EDP", font_size=45).next_to(main_scene.tipos[0], DR).shift(RIGHT)
        edp_expanded = Text("Ecuación Diferencial Parcial", font_size=25, color=GRAY).next_to(edp, DOWN)
        eqs_ord = VGroup(MathTex(r"\frac{d^2y}{dx^2}-4x\frac{dy}{dx}+5y=\cos(x)"),
                        MathTex(r"x\frac{d^3y}{dx^3}-\left(\frac{dy}{dx}\right)^4+y=0"),
                        MathTex(r"x^5\frac{d^4y}{dx^4}-x^3\frac{d^2y}{dx^2}+6y=0")).arrange_submobjects(DOWN, buff=0.75).scale(0.65).next_to(edo_expanded, DOWN).shift(0.5*DOWN)
        eqs_par = VGroup(MathTex(r"\frac{\partial^2u}{\partial x^2}+\frac{\partial^2u}{\partial y^2}=0"),
                        MathTex(r"\frac{\partial^2u}{\partial x^2}=\frac{\partial^2u}{\partial t^2}-2\frac{\partial u}{\partial t}"),
                        MathTex(r"\frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x}")).arrange_submobjects(DOWN, buff=0.75).scale(0.65).next_to(edp_expanded, DOWN).shift(0.5*DOWN)
        
        eqs_ord[0][0][4:6].set_color(GREEN), eqs_ord[0][0][13:15].set_color(GREEN), eqs_ord[1][0][5:7].set_color(GREEN), eqs_ord[1][0][13:15].set_color(GREEN), eqs_ord[2][0][6:8].set_color(GREEN), eqs_ord[2][0][16:18].set_color(GREEN)

        eqs_par[0][0][4:6].set_color(GREEN), eqs_par[0][0][12:14].set_color(RED), eqs_par[1][0][4:6].set_color(GREEN), eqs_par[1][0][12:14].set_color(BLUE), eqs_par[1][0][20:22].set_color(BLUE), eqs_par[2][0][3:5].set_color(RED), eqs_par[2][0][10:12].set_color(GREEN)

        tipos_tipo = VGroup(main_scene.tipos[0], edo, edo_expanded, edp, edp_expanded, eqs_ord, eqs_par)
        main_scene.tipos_tipo = tipos_tipo.copy().scale(1/1.75).move_to(main_scene.center).shift((tipos_tipo[0].get_center()-main_scene.tipos[2].get_center()[1])*DOWN).shift(LEFT*0.85)
        main_scene.tipos_tipo[0].color = BLACK
        main_scene.tipos_tipo[2].scale(0.75)
        main_scene.tipos_tipo[4].scale(0.75)
        main_scene.tipos_tipo[1:3].shift(0.55*RIGHT)
        main_scene.tipos_tipo[5].shift(0.55*RIGHT)
        main_scene.tipos_tipo[3:5].shift(0.55*LEFT)
        main_scene.tipos_tipo[6].shift(0.55*LEFT)
        main_scene.tipos_tipo[5].arrange_submobjects(DOWN, buff=0.8).next_to(main_scene.tipos_tipo[1], DOWN, buff=0.9)
        main_scene.tipos_tipo[6].arrange_submobjects(DOWN, buff=0.8).next_to(main_scene.tipos_tipo[3], DOWN, buff=0.9)

        font = 25
        ed = MathTex(r"\frac{dy}{dx}", "=", "0.2xy", font_size=font, color=BLACK)
        ed[0].set_color(GREEN)
        ed_2 = MathTex(r"\frac{d^2y}{dx^2}", "=", "0.2xy", r"\frac{dy}{dx}", font_size=font, color=BLACK)
        ed_2[0].set_color(GREEN)
        ed_3 = MathTex(r"\frac{d^2y}{dx^2}", "+", r"5", r"\left(", r"\frac{dy}{dx}", r"\right)^3", r"-4y", "=", "e^x", font_size=font, color=BLACK)
        ed_3[0].set_color(GREEN)
        ed_4 = MathTex(r"M(x,y)dx", r"+", r"N(x,y)dy", r"=", "0", font_size=font, color=BLACK)
        ed_5 = MathTex(r"F(x,y,y',y'',...,", r"y^n)", r"=", r"0", font_size=font, color=BLACK)
        ed_5[1][:-1].set_color(GREEN)
        ed_6 = MathTex(r"\frac{d^2y}{dx^2}", r"+", r"5", r"\left(\frac{dy}{dx}\right)^3", r"-", r"4y", r"-", r"e^x", r"=", r"0", font_size=font, color=BLACK)
        ed_6[0].set_color(GREEN)
        ed_9 = MathTex(r"\frac{d^ny}{dx^n}", r"=", r"F(x,y,y',y'',...,", r"y^{(n-1)})", font_size=font, color=BLACK)
        ed_9[0].set_color(GREEN)
        ed_10 = MathTex(r"\frac{d^2y}{dx^2}", r"=", r"-", r"5", r"\left(\frac{dy}{dx}\right)^3", r"+", r"4y", r"+", r"e^x", font_size=font, color=BLACK)
        ed_10[0].set_color(GREEN)
        eds = VGroup(ed, ed_2, ed_3, ed_4, ed_5, ed_6, ed_9, ed_10).arrange(DOWN).shift(0.6*DOWN)
        main_scene.orden = VGroup(eds)
        main_scene.orden[0].scale(0.7).shift(0.7*DOWN)
        
        main_scene.add(main_scene.tipos_tipo, main_scene.title, main_scene.tipos[1:], main_scene.orden)

    def construct(main_scene):
        with main_scene.voiceover(text="El último criterio para clasificar ecuaciones diferenciales <bookmark mark='INTRO'/> es la linealidad, una ecuación diferencial es lineal cuando se ve de la siguiente <bookmark mark='ED'/> forma. En ella podemos identificar a la variable <bookmark mark='Y'/> dependiente y sus derivadas y cada una multiplica a <bookmark mark='A'/> un coeficiente a sub n que son funciones de la variable independiente x y <bookmark mark='G'/> además hay una función g que solo depende de la variable independiente.") as tracker:
            main_scene.center_2 = main_scene.tipos[2].get_center()
            main_scene.wait_until_bookmark('INTRO')
            main_scene.play(main_scene.tipos[2].animate.move_to(main_scene.title.get_center()).scale(1.75).set_color(RED), main_scene.orden.animate.set_opacity(0), main_scene.tipos_tipo.animate.set_opacity(0), main_scene.title.animate.set_opacity(0), main_scene.tipos[1].animate.set_opacity(0), run_time=1.75)
            main_scene.wait_until_bookmark('ED')
            ed_1 = MathTex(r"a_n(x)\frac{d^ny}{dx^n}", r"+", r"a_{n-1}(x)\frac{d^{n-1}y}{dx^{n-1}}", r"+", r"...", r"+", r"a_1(x)", r"\frac{dy}{dx}", r"+", r"a_0(x)y", r"=", r"g(x)", font_size=45)
            main_scene.play(Write(ed_1))
            main_scene.wait_until_bookmark('Y')
            main_scene.play(ed_1[9][5].animate.set_color(BLUE), FocusOn(ed_1[9][5]), run_time=1.2)
            main_scene.play(ed_1[0][5:].animate.set_color(BLUE), ed_1[2][7:].animate.set_color(BLUE), ed_1[7].animate.set_color(BLUE), FocusOn(ed_1[0][5:]), FocusOn(ed_1[2][7:]), FocusOn(ed_1[7]))
            main_scene.wait_until_bookmark('A')
            main_scene.play(ed_1[0][:5].animate.set_color(RED), ed_1[2][:7].animate.set_color(RED), ed_1[6].animate.set_color(RED), ed_1[9][:-1].animate.set_color(RED), FocusOn(ed_1[0][:5]), FocusOn(ed_1[2][:7]), FocusOn(ed_1[6]), FocusOn(ed_1[9][:-1]), run_time=1.5)
            main_scene.wait_until_bookmark('G')
            main_scene.play(ed_1[-1].animate.set_color(GREEN), FocusOn(ed_1[-1]))

        main_scene.wait(0.5)

        with main_scene.voiceover(text="En palabras más simples podemos decir <bookmark mark='INTRO'/> que una ecuación diferencial es lineal <bookmark mark='ED_TRANSFORM'/> cuando tenemos la función <bookmark mark='INDICATE'/> incógnita y y sus derivadas multiplicadas <bookmark mark='X'/> por funciones que solamente dependen de x.") as tracker:
            main_scene.wait_until_bookmark('INTRO')
            ed_2 = MathTex(r"\sin(x)", r"\frac{d^2y}{dx^2}", r"-", r"2", r"\frac{dy}{dx}", r"+", r"5x", r"y", r"=", r"0", font_size=45)
            main_scene.play(TransformMatchingTex(ed_1, ed_2), run_time=tracker.time_until_bookmark('ED_TRANSFORM'))
            main_scene.wait_until_bookmark('INDICATE')
            main_scene.play(LaggedStart(AnimationGroup(ed_2[7].animate.set_color(BLUE), FocusOn(ed_2[7])), AnimationGroup(ed_2[4].animate.set_color(BLUE), ed_2[1].animate.set_color(BLUE), FocusOn(ed_2[4]), FocusOn(ed_2[1])), lag_ratio=0.4))
            main_scene.wait_until_bookmark('X')
            main_scene.play(ed_2[0].animate.set_color(GREEN), ed_2[3].animate.set_color(GREEN), ed_2[6].animate.set_color(GREEN), FocusOn(ed_2[0]), FocusOn(ed_2[3]), FocusOn(ed_2[6]))

        main_scene.wait(0.5)

        with main_scene.voiceover(text="Algunos ejemplos de ecuaciones diferenciales <bookmark mark='INTRO'/> lineales son los siguientes:") as tracker:
            ed_3 = MathTex(r"x^3", r"\frac{d^3y}{dx^3}", r"+", r"x", r"\frac{dy}{dx}", r"-", r"5", r"y", r"=", r"e^x", font_size=45)
            ed_4 = MathTex(r"5x", r"\frac{d^2y}{dx^2}", r"+", r"4x", r"\frac{dy}{dx}", r"-", r"12", r"y", r"=", r"5x^2", font_size=45)
            ed_5 = MathTex(r"\frac{d^2y}{dx^2}", r"+", r"\frac{dy}{dx}", r"-", r"2", r"y", r"=", r"0", font_size=45)
            eds = VGroup(ed_3, ed_4, ed_5).arrange_submobjects(DOWN, buff=0.6).shift(DOWN*0.6)
            main_scene.wait_until_bookmark('INTRO')
            main_scene.play(ReplacementTransform(ed_2, eds))
        
        main_scene.wait(0.2)

        blues = AnimationGroup(ed_3[1].animate.set_color(BLUE), ed_3[4].animate.set_color(BLUE), ed_3[7].animate.set_color(BLUE), ed_4[1].animate.set_color(BLUE), ed_4[4].animate.set_color(BLUE), ed_4[7].animate.set_color(BLUE), ed_5[0].animate.set_color(BLUE), ed_5[2].animate.set_color(BLUE), ed_5[5].animate.set_color(BLUE))
        greens = AnimationGroup(ed_3[0].animate.set_color(GREEN), ed_3[3].animate.set_color(GREEN), ed_3[6].animate.set_color(GREEN), ed_4[0].animate.set_color(GREEN), ed_4[3].animate.set_color(GREEN), ed_4[6].animate.set_color(GREEN), ed_5[4].animate.set_color(GREEN))

        with main_scene.voiceover(text="En todas ellas podemos ver de color azul a la función y y a sus derivadas y de color verde a los coeficientes que dependen de x.") as tracker:
            main_scene.play(blues, greens, run_time=2.5)

        main_scene.wait(0.75)

        with main_scene.voiceover(text="Por otro lado algunos ejemplos de ecuaciones diferenciales no <bookmark mark='WRITE'/> lineales son: los siguientes, en este caso esta no es una ecuación diferencial lineal porque la derivada de y respecto a x multiplica <bookmark mark='WRONG'/> a una función que depende de y y como acabamos de establecer los coeficientes de una ecuación diferencial <bookmark mark='BAD'/> lineal no pueden depender de la función incógnita. <bookmark mark='SEGUNDA'/> La siguiente ecuación no es lineal porque incluye una función no lineal de <bookmark mark='SENO'/> y como lo es el seno. Y finalmente esta última ecuación tampoco es lineal porque la función <bookmark mark='CUADRADO'/> incógnita está elevada al cuadrado.") as tracker:
            main_scene.play(FadeOut(ed_3, ed_4, ed_5), run_time=tracker.time_until_bookmark('WRITE'))
            ed_6 = MathTex(r"(1-y)", r"\frac{dy}{dx}", r"+", r"2y", r"=", r"e^x", font_size=50)
            main_scene.play(Write(ed_6))
            main_scene.wait_until_bookmark('WRONG')
            main_scene.play(ed_6[:2].animate.set_color(RED), FocusOn(ed_6[:2]), run_time=1.5)
            main_scene.wait_until_bookmark('BAD')
            cross = SVGMobject(r'D:\Youtube\ED\Capitulo 1\resources\circle_xmark.svg', fill_opacity=1, stroke_width=0, fill_color=RED, height=2.5, width=2.5)
            cross.z_index = 100
            main_scene.play(FadeIn(cross), run_time=1.5)
            main_scene.wait_until_bookmark('SEGUNDA')
            ed_7 = MathTex(r"\frac{d^2y}{dx^2}", r"+", r"sen(y)", r"=", r"0", font_size=50).shift(0.5*DOWN)
            main_scene.play(ed_6.animate.shift(UP), FadeOut(cross), Write(ed_7))
            main_scene.wait_until_bookmark('SENO')
            main_scene.play(ed_7[2].animate.set_color(RED), FocusOn(ed_7[2]))
            ed_8 = MathTex(r"\frac{d^4y}{dx^4}", r"+", r"y^2", r"=", r"0", font_size=50).shift(0.5*DOWN)
            ed_8.set_opacity(0)
            main_scene.play(ed_8.animate.set_opacity(1).shift(1.5*DOWN), run_time=1.5)
            main_scene.wait_until_bookmark('CUADRADO')
            main_scene.play(ed_8[2].animate.set_color(RED), FocusOn(ed_8[2]))
            nolinear = VGroup(ed_6, ed_7, ed_8)

        with main_scene.voiceover(text="De esta forma ya sabemos cuales son las características para determinar si una ecuación diferencial es lineal o no") as tracker:
            main_scene.wait(0.5)
            ed_9 = MathTex(r"x^3", r"\frac{d^3y}{dx^3}", r"+", r"x", r"\frac{dy}{dx}", r"-", r"5", r"y", r"=", r"e^x", font_size=45).set_color(GREEN)
            ed_10 = MathTex(r"5x", r"\frac{d^2y}{dx^2}", r"+", r"4x", r"\frac{dy}{dx}", r"-", r"12", r"y", r"=", r"5x^2", font_size=45).set_color(GREEN)
            ed_11 = MathTex(r"\frac{d^2y}{dx^2}", r"+", r"\frac{dy}{dx}", r"-", r"2", r"y", r"=", r"0", font_size=45).set_color(GREEN)
            linear = VGroup(ed_9, ed_10, ed_11).arrange_submobjects(DOWN, buff=0.6).shift(0.7*DOWN+2.5*LEFT).scale(0.75)
            t1 = Text("Lineales").next_to(linear, UP).scale(0.8).shift(0.2*UP)
            t2 = Text("No Lineales").move_to(t1.get_center()).shift(5*RIGHT).scale(0.8)
            main_scene.play(nolinear.animate.shift(2.5*RIGHT+0.2*DOWN).set_color(RED).scale(0.75), FadeIn(linear), FadeIn(t1), FadeIn(t2), run_time=2.5)
        
        linealidad = VGroup(linear, nolinear, t1, t2, main_scene.tipos[2])
        main_scene.play(linealidad[:-1].animate.next_to(main_scene.center_2, DOWN).scale(1/1.75).shift(0.45*UP), linealidad[-1].animate.move_to(main_scene.center_2).scale(1/1.75).set_color(BLACK), main_scene.orden.animate.set_opacity(1), main_scene.tipos_tipo.animate.set_opacity(1), main_scene.title.animate.set_opacity(1), main_scene.tipos[1].animate.set_opacity(1))
        main_scene.wait()
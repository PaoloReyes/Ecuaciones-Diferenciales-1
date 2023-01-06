from manim import config, MathTex, Text, WHITE, BLACK, DOWN, LEFT, RIGHT, VGroup, DL, GRAY, DR, BLUE, UP, GREEN, RED, Write, Indicate, TransformMatchingTex, FadeOut, FadeIn, Flash
from manim_voiceover import VoiceoverScene

config.background_color = WHITE
MathTex.set_default(color=BLACK)
Text.set_default(color=BLACK)

class Orden(VoiceoverScene):
    def setup(main_scene):
        from manim_voiceover.services.gtts import GTTSService
        from manim_voiceover.services.recorder import RecorderService

        #main_scene.set_speech_service(GTTSService("es", transcription_model='base'))
        main_scene.set_speech_service(RecorderService())

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
        
        main_scene.add(main_scene.tipos_tipo, main_scene.title, main_scene.tipos[1:])

    def construct(main_scene):
        with main_scene.voiceover(text="Es momento de hablar del segundo criterio para clasificar ecuaciones diferenciales. <bookmark mark='INTRO'/> El orden es un valor que nos indica cual es la mayor derivada de la ecuación. Por ejemplo, si tenemos a la ecuación <bookmark mark='ED'/> diferencial donde la derivada de y con respecto a x es igual <bookmark mark='ED_END'/> a 0.2xy podemos catalogarla como de primer orden porque su <bookmark mark='MAX'/> máxima derivada es la primera derivada de y <bookmark mark='MAX_END'/>, por otro lado si tenemos esta <bookmark mark='ED_2_BEGIN'/> ecuación diferencial entonces tenemos una ecuación diferencial de segundo <bookmark mark='ED_2_END'/> orden porque su máxima derivada es la segunda derivada de y") as tracker:
            main_scene.wait_until_bookmark('INTRO')
            main_scene.play(main_scene.tipos[1].animate.to_edge(UP).scale(1.75).set_color(RED), main_scene.tipos[2].animate.set_opacity(0), main_scene.tipos_tipo.animate.set_opacity(0), main_scene.title.animate.set_opacity(0), run_time=1.75)
            ed = MathTex(r"\frac{dy}{dx}", "=", "0.2xy", font_size=80, color=BLACK)
            main_scene.wait_until_bookmark('ED')
            main_scene.play(Write(ed), run_time=tracker.time_until_bookmark('ED_END'))
            main_scene.wait_until_bookmark('MAX')
            main_scene.play(Indicate(ed[0], color=BLUE), run_time=tracker.time_until_bookmark('MAX_END'))
            ed_2 = MathTex(r"\frac{d^2y}{dx^2}", "=", "0.2xy", r"\frac{dy}{dx}", font_size=80, color=BLACK)
            main_scene.wait_until_bookmark('ED_2_BEGIN')
            main_scene.play(TransformMatchingTex(ed, ed_2))
            main_scene.wait_until_bookmark('ED_2_END')
            main_scene.play(Indicate(ed_2[0], color=BLUE), run_time=tracker.get_remaining_duration())

        main_scene.wait(0.4)

        with main_scene.voiceover(text="Es importante notar que el orden no es lo mismo que el grado en una ecuación diferencial y por lo tanto no debe ser confundido, por ejemplo en la siguiente <bookmark mark='INTRO'/> ecuación se podría confundir el orden con el grado, sorprendentemente el orden de esta ecuación es 2 y no 3, esto se debe a <bookmark mark='ED_3_WAIT'/> que el 3 que está al lado de la derivada no es su orden si no que es su grado y signfica que se está elevando al cubo, por lo tanto la derivada de mayor orden <bookmark mark='ED_3_END'/> y por ende el orden de la ecuación es el orden 2.") as tracker:
            main_scene.wait_until_bookmark('INTRO')
            ed_3 = MathTex(r"\frac{d^2y}{dx^2}", "+", r"5", r"\left(", r"\frac{dy}{dx}", r"\right)^3", r"-4y", "=", "e^x", font_size=80, color=BLACK)
            main_scene.play(TransformMatchingTex(ed_2, ed_3), run_time=1.3)
            main_scene.wait_until_bookmark('ED_3_WAIT')
            main_scene.play(ed_3[3].animate.scale(1.15), ed_3[4].animate.scale(1.15), ed_3[5][1].animate.set_color(RED).scale(1.15), ed_3[5][0].animate.scale(1.15), run_time=2)
            main_scene.play(ed_3[3].animate.scale(0.87), ed_3[4].animate.scale(0.87), ed_3[5][1].animate.set_color(BLACK).scale(0.87), ed_3[5][0].animate.scale(0.87), run_time=2)
            main_scene.wait_until_bookmark('ED_3_END')
            main_scene.play(Indicate(ed_3[0], color=BLUE), run_time=tracker.get_remaining_duration())

        main_scene.wait(0.4)

        with main_scene.voiceover(text="Hay algunos tips para identificar el orden de una ecuación diferencial ordinaria por ejemplo en ocasiones <bookmark mark='INTRO'/> se suele usar una notación diferencial <bookmark mark='ED_4_BEGIN'/> para describir ecuaciones diferenciales de primer orden <bookmark mark='ED_4_END'/> en este tipo de notación se escribe una función <bookmark mark='M_BEGIN'/> multivariable M multiplicada por dx <bookmark mark='M_END'/> y otra función multivariable N multiplicada por dy <bookmark mark='N_END'/>, en esos casos las ecuaciones siempre son de primer orden. En otros ejemplos <bookmark mark='WAIT_GENERAL'/> podemos encontrar ecuaciones diferenciales de n-ésimo orden por su forma general donde tenemos una <bookmark mark='GENERAL_BEGIN'/> función igualada a 0 cuyas variables son x, y, la derivada de y, la segunda derivada de y y así hasta la enésima derivada de y <bookmark mark='GENERAL_END'/> y para identificar el orden de estas ecuaciones miramos cada derivada como lo hemos <bookmark mark='ED_6_BEGIN'/> hecho hasta el momento y buscamos la más profunda <bookmark mark='ED_6_END'/> , finalmente podemos encontrar ecuaciones diferenciales en su forma normal <bookmark mark='NORMAL_BEGIN'/> que no es más que la forma general despejada para la derivada de mayor orden y en ese caso el orden se encuentra <bookmark mark='NORMAL_HIGHLIGHT'/> simplemente mirando al término que está solo en la igualdad.") as tracker:
            main_scene.wait_until_bookmark('INTRO')
            ed_4 = MathTex(r"M(x,y)dx", r"+", r"N(x,y)dy", r"=", "0", font_size=80, color=BLACK)
            main_scene.play(FadeOut(ed_3), runt_time=1.3)
            main_scene.wait_until_bookmark('ED_4_BEGIN')
            main_scene.play(Write(ed_4), run_time=tracker.time_until_bookmark('ED_4_END'))
            main_scene.wait_until_bookmark('M_BEGIN')
            main_scene.play(Indicate(ed_4[0], color=BLUE, scale_factor=1.15), run_time=tracker.time_until_bookmark('M_END'))
            main_scene.play(Indicate(ed_4[2], color=GREEN, scale_factor=1.15), run_time=tracker.time_until_bookmark('N_END'))
            main_scene.wait_until_bookmark('WAIT_GENERAL')
            main_scene.play(FadeOut(ed_4), run_time=tracker.time_until_bookmark('GENERAL_BEGIN'))
            ed_5 = MathTex(r"F(x,y,y',y'',...,", r"y^n)", r"=", r"0", font_size=80, color=BLACK)
            main_scene.play(Write(ed_5), run_time=tracker.time_until_bookmark('GENERAL_END'))
            ed_6 = MathTex(r"\frac{d^2y}{dx^2}", r"+", r"5", r"\left(\frac{dy}{dx}\right)^3", r"-", r"4y", r"-", r"e^x", r"=", r"0", font_size=80, color=BLACK).shift(1.2*DOWN)
            main_scene.play(ed_5.animate.shift(1.2*UP), FadeIn(ed_6))
            main_scene.play(ed_6[0].animate.scale(1.2).set_color(GREEN), ed_6[3].animate.scale(1.2).set_color(RED), run_time=tracker.time_until_bookmark('ED_6_BEGIN')/2)
            main_scene.play(ed_6[0].animate.scale(0.83).set_color(GREEN), ed_6[3].animate.scale(0.83).set_color(BLACK), run_time=tracker.time_until_bookmark('ED_6_BEGIN'))
            main_scene.play(Flash(ed_6[0], flash_radius=1, color=BLUE, line_length=0.45), run_time=tracker.time_until_bookmark('ED_6_END'))
            ed_7 = MathTex(r"\frac{d^ny}{dx^n}", r"=", r"F(x,y,y',y'',...,", r"y^{(n-1)})", font_size=80, color=BLACK).shift(1.35*UP)
            ed_8 = MathTex(r"\frac{d^2y}{dx^2}", r"=", r"-", r"5", r"\left(\frac{dy}{dx}\right)^3", r"+", r"4y", r"+", r"e^x", font_size=80, color=BLACK).shift(1.35*DOWN)
            main_scene.wait_until_bookmark('NORMAL_BEGIN')
            main_scene.play(TransformMatchingTex(ed_5, ed_7), TransformMatchingTex(ed_6, ed_8), run_time=2)
            main_scene.wait_until_bookmark('NORMAL_HIGHLIGHT')
            main_scene.play(Indicate(ed_7[0], color=BLUE), Indicate(ed_8[0], color=BLUE), run_time=tracker.get_remaining_duration())

        main_scene.wait(0.5)

        with main_scene.voiceover(text="Estos son solo algunos tips para identificar más facilmente el orden de una ecuación diferencial, pero en general es necesario hacer una inspección completa para determinar su orden.") as tracker:
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
            main_scene.play(TransformMatchingTex(ed_7, eds[6]), TransformMatchingTex(ed_8, eds[7]), FadeIn(eds[:-2]), run_time=1.5)
        
        orden = VGroup(eds, main_scene.tipos[1])
        main_scene.play(orden[0].animate.scale(0.7).shift(0.7*DOWN), orden[1].animate.move_to(main_scene.center_1).scale(0.57).set_color(BLACK), main_scene.tipos[2].animate.set_opacity(1), main_scene.title.animate.set_opacity(1), main_scene.tipos_tipo.animate.set_opacity(1))
        main_scene.wait(0.2)
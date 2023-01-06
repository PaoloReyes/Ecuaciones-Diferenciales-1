from manim import Text, VGroup, MathTex, BLUE, RED, DL, DR, VGroup, ReplacementTransform, FadeIn, LaggedStart, DOWN, RIGHT, LEFT, UP, GRAY, config, WHITE, BLACK, GREEN, AnimationGroup, FocusOn, Indicate, Circumscribe
from manim_voiceover import VoiceoverScene

config.background_color = WHITE
MathTex.set_default(color=BLACK)
Text.set_default(color=BLACK)

class Tipos(VoiceoverScene):
    def setup(main_scene):
        from manim_voiceover.services.gtts import GTTSService
        from manim_voiceover.services.recorder import RecorderService

        #main_scene.set_speech_service(GTTSService("es", transcription_model='base'))
        main_scene.set_speech_service(RecorderService())

        main_scene.title = Text("Clasificación", font_size=80, color=BLUE).to_edge(UP)
        main_scene.tipos = VGroup(Text("Tipo"), Text("Orden"), Text("Linealidad")).arrange_submobjects(RIGHT, buff=1.5).next_to(main_scene.title, DOWN).shift(0.5*DOWN+RIGHT)
        main_scene.tipos[0].shift(0.85*LEFT)
        main_scene.add(main_scene.title, main_scene.tipos)

    def construct(main_scene):
        with main_scene.voiceover(text="La clasificación por tipo es quizá una de las más fáciles de comprender ya que solo se divide <bookmark mark='A'/> en dos, EDO y EDP, EDO <bookmark mark='WAIT_EDO'/> significa ecuación diferencial ordinaria <bookmark mark='EDO_MEANING'/>, y son ecuaciones que solo contienen derivadas respecto a una variable independiente <bookmark mark='DISPLAY_EDO'/>, se pueden identificar facilmente con solo observar las derivadas y verificar que todas las variables con respecto a las que se derive <bookmark mark='INDICATE_DX'/> sean la misma, mientras que las EDP que vienen de ecuación diferencial parcial <bookmark mark='EDP_MEANING'/>, son aquellas que contienen derivadas respecto a dos o más variables independientes <bookmark mark='DISPLAY_EDP'/>, estas se pueden identificar haciendo el mismo análisis que con las ecuaciones diferenciales ordinarias y verificar si hay almenos dos variables <bookmark mark='INDICATE_DX_2'/> diferentes. Otra forma de identificarlas es observar <bookmark mark='WAIT_SYMBOL'/> si la ecuación diferencial usa el símbolo δ en <bookmark mark='INDICATE_DELTA'/> lugar de una d esto quiere decir que estamos tratando con derivadas parciales y en la mayoría de los casos tambien significa que estamos ante una ecuación diferencial parcial. Las ecuaciones diferenciales <bookmark mark='WAIT_DELTA'/> ordinarias son las más comunes y las que se usan en la mayoría de las aplicaciones básicas, por lo que en esta serie nos enfocaremos en ellas y posiblemente en un futuro <bookmark mark='WAIT_HIGHLIGHT'/> haga un video sobre sus extrañas hermanas las ecuaciones diferenciales parciales.") as tracker:
            main_scene.center = main_scene.tipos[0].get_center()
            main_scene.center_1 = main_scene.tipos[1].get_center()
            main_scene.play(main_scene.tipos[0].animate.set_color(RED).move_to(main_scene.title.get_center()).scale(1.75), *[obj.animate.set_opacity(0) if obj != main_scene.tipos else obj[1:].animate.set_opacity(0) for obj in main_scene.mobjects])
            main_scene.wait_until_bookmark('A')
            edo = Text("EDO", font_size=45).next_to(main_scene.tipos[0], DL).shift(LEFT)
            edp = Text("EDP", font_size=45).next_to(main_scene.tipos[0], DR).shift(RIGHT)
            main_scene.play(ReplacementTransform(main_scene.tipos[0].copy(), edo), ReplacementTransform(main_scene.tipos[0].copy(), edp))
            main_scene.wait_until_bookmark('WAIT_EDO')
            edo_expanded = Text("Ecuación Diferencial Ordinaria", font_size=25, color=GRAY).next_to(edo, DOWN)
            main_scene.play(ReplacementTransform(edo.copy(), edo_expanded), run_time=tracker.time_until_bookmark('EDO_MEANING'))
            eqs_ord = VGroup(MathTex(r"\frac{d^2y}{dx^2}-4x\frac{dy}{dx}+5y=\cos(x)"),
                        MathTex(r"x\frac{d^3y}{dx^3}-\left(\frac{dy}{dx}\right)^4+y=0"),
                        MathTex(r"x^5\frac{d^4y}{dx^4}-x^3\frac{d^2y}{dx^2}+6y=0")).arrange_submobjects(DOWN, buff=0.75).scale(0.65).next_to(edo_expanded, DOWN).shift(0.5*DOWN)
            main_scene.play(LaggedStart(*[FadeIn(eq) for eq in eqs_ord], lag_ratio=0.5))
            main_scene.wait_until_bookmark('DISPLAY_EDO')
            main_scene.play(LaggedStart(AnimationGroup(FocusOn(eqs_ord[0][0][4:6], run_time=0.5), eqs_ord[0][0][4:6].animate.set_color(GREEN)), AnimationGroup(FocusOn(eqs_ord[0][0][13:15], run_time=0.5), eqs_ord[0][0][13:15].animate.set_color(GREEN)), AnimationGroup(FocusOn(eqs_ord[1][0][5:7], run_time=0.5), eqs_ord[1][0][5:7].animate.set_color(GREEN)), AnimationGroup(FocusOn(eqs_ord[1][0][13:15], run_time=0.5), eqs_ord[1][0][13:15].animate.set_color(GREEN)),  AnimationGroup(FocusOn(eqs_ord[2][0][6:8], run_time=0.5), eqs_ord[2][0][6:8].animate.set_color(GREEN)), AnimationGroup(FocusOn(eqs_ord[2][0][16:18], run_time=0.5), eqs_ord[2][0][16:18].animate.set_color(GREEN)), lag_ratio=tracker.time_until_bookmark('INDICATE_DX')/16), run_time=tracker.time_until_bookmark('INDICATE_DX'))
            edp_expanded = Text("Ecuación Diferencial Parcial", font_size=25, color=GRAY).next_to(edp, DOWN)
            main_scene.play(ReplacementTransform(edp.copy(), edp_expanded), run_time=tracker.time_until_bookmark('EDP_MEANING'))
            eqs_par = VGroup(MathTex(r"\frac{\partial^2u}{\partial x^2}+\frac{\partial^2u}{\partial y^2}=0"),
                        MathTex(r"\frac{\partial^2u}{\partial x^2}=\frac{\partial^2u}{\partial t^2}-2\frac{\partial u}{\partial t}"),
                        MathTex(r"\frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x}")).arrange_submobjects(DOWN, buff=0.75).scale(0.65).next_to(edp_expanded, DOWN).shift(0.5*DOWN)
            main_scene.play(LaggedStart(*[FadeIn(eq) for eq in eqs_par], lag_ratio=0.5))
            main_scene.wait_until_bookmark('DISPLAY_EDP')
            main_scene.play(LaggedStart(AnimationGroup(FocusOn(eqs_par[0][0][4:6], run_time=0.5), eqs_par[0][0][4:6].animate.set_color(GREEN)), AnimationGroup(FocusOn(eqs_par[0][0][12:14], run_time=0.5), eqs_par[0][0][12:14].animate.set_color(RED)), AnimationGroup(FocusOn(eqs_par[1][0][4:6], run_time=0.5), eqs_par[1][0][4:6].animate.set_color(GREEN)), AnimationGroup(FocusOn(eqs_par[1][0][12:14], run_time=0.5), eqs_par[1][0][12:14].animate.set_color(BLUE)),  AnimationGroup(FocusOn(eqs_par[1][0][20:22], run_time=0.5), eqs_par[1][0][20:22].animate.set_color(BLUE)), AnimationGroup(FocusOn(eqs_par[2][0][3:5], run_time=0.5), eqs_par[2][0][3:5].animate.set_color(RED)), AnimationGroup(FocusOn(eqs_par[2][0][10:12], run_time=0.5), eqs_par[2][0][10:12].animate.set_color(GREEN)), lag_ratio=tracker.time_until_bookmark('INDICATE_DX_2')/16), run_time=tracker.time_until_bookmark('INDICATE_DX_2'))
            main_scene.wait_until_bookmark('WAIT_SYMBOL')
            main_scene.play(Indicate(eqs_par[0][0][4]), Indicate(eqs_par[0][0][0]), Indicate(eqs_par[0][0][8]), Indicate(eqs_par[0][0][12]), Indicate(eqs_par[1][0][0]), Indicate(eqs_par[1][0][4]), Indicate(eqs_par[1][0][8]), Indicate(eqs_par[1][0][12]), Indicate(eqs_par[1][0][17]), Indicate(eqs_par[1][0][20]), Indicate(eqs_par[2][0][0]), Indicate(eqs_par[2][0][3]), Indicate(eqs_par[2][0][7]), Indicate(eqs_par[2][0][10]), run_time=tracker.time_until_bookmark('INDICATE_DELTA'))
            main_scene.wait_until_bookmark('WAIT_DELTA')
            main_scene.play(Circumscribe(VGroup(edo, edo_expanded, eqs_ord), color=BLUE), run_time=5)
            main_scene.wait_until_bookmark('WAIT_HIGHLIGHT')
            main_scene.play(Circumscribe(VGroup(edp, edp_expanded, eqs_par), color=BLUE), run_time=2.5)
            main_scene.wait_for_voiceover()
        
        tipos_tipo = VGroup(main_scene.tipos[0], edo, edo_expanded, edp, edp_expanded, eqs_ord, eqs_par)
        main_scene.tipos_tipo = tipos_tipo.copy().scale(1/1.75).move_to(main_scene.center).shift((tipos_tipo[0].get_center()-main_scene.tipos[2].get_center()[1])*DOWN)
        main_scene.tipos_tipo[0].color = BLACK
        main_scene.tipos_tipo[2].scale(0.75)
        main_scene.tipos_tipo[4].scale(0.75)
        main_scene.tipos_tipo[1:3].shift(0.55*RIGHT)
        main_scene.tipos_tipo[5].shift(0.55*RIGHT)
        main_scene.tipos_tipo[3:5].shift(0.55*LEFT)
        main_scene.tipos_tipo[6].shift(0.55*LEFT)
        main_scene.tipos_tipo[5].arrange_submobjects(DOWN, buff=0.8).next_to(main_scene.tipos_tipo[1], DOWN, buff=0.9)
        main_scene.tipos_tipo[6].arrange_submobjects(DOWN, buff=0.8).next_to(main_scene.tipos_tipo[3], DOWN, buff=0.9)
        main_scene.play(ReplacementTransform(tipos_tipo, main_scene.tipos_tipo), main_scene.tipos[1].animate.set_opacity(1), main_scene.tipos[2].animate.set_opacity(1), main_scene.title.animate.set_opacity(1), run_time=1.3)
        main_scene.wait(0.2)
from manim import VGroup, MathTex, FadeTransform, Text, LaggedStart, FadeOut, Write, UP, DOWN, LEFT, RIGHT, BLUE, GREEN, ORIGIN, config, WHITE, BLACK
from manim_voiceover import VoiceoverScene

config.background_color = WHITE
MathTex.set_default(color=BLACK)
Text.set_default(color=BLACK)

class Categorias(VoiceoverScene):
    def setup(main_scene):
        from manim_voiceover.services.gtts import GTTSService
        from manim_voiceover.services.recorder import RecorderService

        # main_scene.set_speech_service(GTTSService("es", transcription_model='base'))
        main_scene.set_speech_service(RecorderService())

        eq_der = MathTex(r"\frac{dy}{dx}", r"=", r"0.2x", r"e^{0.1x^2}").scale(1.2).shift(DOWN)
        eq_der[2].color=BLUE
        main_scene.eq_diff = eq_der[:3].copy()
        eq = MathTex(r"y", r"=", r"e^{0.1x^2}").scale(1.2)
        eq_copy = eq[0].copy().next_to(eq_der[2]).shift(0.12*DOWN+0.2*LEFT)
        main_scene.eq_diff = VGroup(main_scene.eq_diff, eq_copy).move_to(ORIGIN)
        main_scene.add(main_scene.eq_diff)

    def construct(main_scene):        
        with main_scene.voiceover(text="Debido a la gran variedad <bookmark mark='A'/> de ecuaciones diferenciales que existen y a los diversos métodos para resolverlas es <bookmark mark='B'/> necesario clasificarlas para poder trabajar con ellas de una forma más ordenada, podemos <bookmark mark='C'/> separarlas en 3 principales categorías:") as tracker:
            eqs = VGroup(MathTex(r"(1-x)y''-4xy'+5y=\cos(x)"),
                        MathTex(r"x\frac{d^3y}{dx^3}-\left(\frac{dy}{dx}\right)^4+y=0"),
                        MathTex(r"t^5y^{(4)}-t^3y''+6y=0"),
                        MathTex(r"\frac{d^2y}{dx^2}+\frac{dy}{dx}+y=\cos(r+u)"),
                        MathTex(r"\frac{d^2y}{dx^2}=\sqrt{1+\left(\frac{dy}{dx}\right)^2}"),
                        MathTex(r"\frac{d^2y}{dx^2}=-\frac{k}{y^2}"),
                        MathTex(r"\sin(\theta)y'''-\cos(\theta)y'=2"),
                        MathTex(r"y''-\left(1-\frac{y'}{3}\right)y'+y=0"),
                        MathTex(r"(y^2-1)dx+xdy=0")).arrange_in_grid(rows=3, cols=3, buff=(1, 1.5)).scale(0.7)
            main_scene.wait_until_bookmark('A')
            main_scene.play(FadeTransform(main_scene.eq_diff, eqs), run_time=tracker.time_until_bookmark('B'))
            main_scene.title = Text("Clasificación", font_size=80, color=BLUE).to_edge(UP)
            main_scene.tipos = VGroup(Text("Tipo"), Text("Orden"), Text("Linealidad")).arrange_submobjects(RIGHT, buff=1.5).next_to(main_scene.title, DOWN).shift(0.5*DOWN+RIGHT)
            main_scene.tipos[0].shift(0.85*LEFT)
            main_scene.wait_until_bookmark('C')
            main_scene.play(LaggedStart(FadeOut(eqs), Write(main_scene.title), Write(main_scene.tipos)))
            main_scene.wait_for_voiceover()
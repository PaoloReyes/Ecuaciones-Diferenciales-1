from manim import VGroup, MathTex, FadeOut, Write, LaggedStart, TransformMatchingTex, Indicate, ApplyWave, FadeIn, config, UP, DOWN, LEFT, RED, GREEN, BLUE, WHITE, BLACK, ORIGIN
from manim_voiceover import VoiceoverScene
from numpy import exp

# Configuración Sub Escena
config.background_color = WHITE
MathTex.set_default(color=BLACK)

class QueSon(VoiceoverScene):
    def setup(main_scene):
        from manim_voiceover.services.gtts import GTTSService
        from manim_voiceover.services.recorder import RecorderService

        main_scene.set_speech_service(RecorderService())
        #main_scene.set_speech_service(GTTSService("es", transcription_model='base'))

        main_scene.eqs=VGroup(MathTex(r"(1-x)y''-4xy'+5y=\cos(x)"),
                        MathTex(r"x\frac{d^3y}{dx^3}-\left(\frac{dy}{dx}\right)^4+y=0"),
                        MathTex(r"t^5y^{(4)}-t^3y''+6y=0"),
                        MathTex(r"\frac{d^2y}{dx^2}+\frac{dy}{dx}+y=\cos(r+u)"),
                        MathTex(r"\frac{d^2y}{dx^2}=\sqrt{1+\left(\frac{dy}{dx}\right)^2}"),
                        MathTex(r"\frac{d^2y}{dx^2}=-\frac{k}{y^2}"),
                        MathTex(r"\sin(\theta)y'''-\cos(\theta)y'=2"),
                        MathTex(r"y''-\left(1-\frac{y'^2}{3}\right)y'+y=0"),
                        MathTex(r"(y^2-1)dx+xdy=0")).arrange_in_grid(rows=3, cols=3, buff=(1, 1.5)).scale(0.7).apply_complex_function(exp)
        main_scene.add(main_scene.eqs)

    def construct(main_scene):
        with main_scene.voiceover(text="Podemos comenzar a hablar de ecuaciones diferenciales partiendo de un ejemplo") as tracker:
            main_scene.play(FadeOut(main_scene.eqs), run_time=tracker.duration)

        with main_scene.voiceover(text="Si tenemos a la función <bookmark mark='A'/> y igual a e elevado a 0.1 x al <bookmark mark='B'/> cuadrado y obtenemos <bookmark mark='C'/> su derivada, vemos que es igual a 0.2 x <bookmark mark='D'/> por e elevado a 0.1 x al cuadrado <bookmark mark='E'/>. Si ponemos ambas funciones en la pantalla nos damos <bookmark mark='F'/> cuenta que la derivada de <bookmark mark='G'/> y es igual a ye <bookmark mark='H'/> multiplicada por un número <bookmark mark='I'/>, entonces podemos sustituir e elevada <bookmark mark='J'/> a la 0.1 x al cuadrado por ye <bookmark mark='K'/> y escribir la relación entre la derivada y la <bookmark mark='L'/> función original en una sola expresión <bookmark mark='M'/>, esto es una ecuación <bookmark mark='N'/> diferencial, no es más que una expresión matemática que guarda <bookmark mark='O'/> la relación entre una función y sus derivadas.") as tracker:
            eq = MathTex(r"y", r"=", r"e^{0.1x^2}").scale(1.2)
            eq_der = MathTex(r"\frac{dy}{dx}", r"=", r"0.2x", r"e^{0.1x^2}").scale(1.2)
            main_scene.wait_until_bookmark('A')
            main_scene.play(Write(eq), run_time=2)
            main_scene.wait_until_bookmark('B')
            main_scene.play(eq.animate.shift(UP), run_time=tracker.time_until_bookmark('C'))
            main_scene.play(TransformMatchingTex(eq, eq_der))
            main_scene.play(Indicate(eq_der[2], color=RED), run_time=tracker.time_until_bookmark('D'))
            main_scene.play(Indicate(eq_der[3], color=RED), run_time=tracker.time_until_bookmark('E'))
            eq = MathTex(r"y", r"= e^{0.1x^2}").scale(1.2).shift(UP)
            main_scene.play(eq_der.animate.shift(DOWN), FadeIn(eq), run_time=tracker.time_until_bookmark('F'))
            main_scene.play(Indicate(eq_der[0], color=RED), run_time=tracker.time_until_bookmark('G'))
            eq_der[3].color=GREEN
            eq[1][1:].color=GREEN
            main_scene.play(Indicate(eq_der[3], color=GREEN), Indicate(eq[1][1:], color=GREEN), run_time=tracker.time_until_bookmark('H'))
            eq_der[2].color=BLUE
            main_scene.play(Indicate(eq_der[2], color=BLUE), run_time=tracker.time_until_bookmark('I'))
            eq_copy = eq[0].copy()
            main_scene.wait_until_bookmark('J')
            main_scene.play(eq_copy.animate.next_to(eq_der[2]).shift(0.12*DOWN+0.2*LEFT), FadeOut(eq_der[3]), FadeOut(eq), run_time=tracker.time_until_bookmark('K'))
            main_scene.eq_diff = eq_der[:3].copy()
            main_scene.add(main_scene.eq_diff)
            eq_der.set_opacity(0)
            main_scene.wait_until_bookmark('L')
            main_scene.eq_diff = VGroup(main_scene.eq_diff, eq_copy)
            main_scene.play(main_scene.eq_diff.animate.move_to(ORIGIN), run_time=tracker.time_until_bookmark('M'))
            main_scene.wait_until_bookmark('N')
            main_scene.play(ApplyWave(main_scene.eq_diff))
            main_scene.wait_until_bookmark('O')
            main_scene.play(Indicate(main_scene.eq_diff[1], color=GREEN), run_time=1)
            main_scene.play(Indicate(main_scene.eq_diff[0][0], color=RED), run_time=1)
            main_scene.wait_for_voiceover()
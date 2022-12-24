from manim import MathTex, VGroup, Write, LaggedStart, config, WHITE, BLACK
from manim_voiceover import VoiceoverScene
from numpy import exp

# Configuración Sub Escena
config.background_color = WHITE
MathTex.set_default(color=BLACK)

class Intro(VoiceoverScene):
    def setup(main_scene):
        from manim_voiceover.services.gtts import GTTSService
        from manim_voiceover.services.recorder import RecorderService
        
        #main_scene.set_speech_service(RecorderService())
        main_scene.set_speech_service(GTTSService("es", transcription_model='base'))

    def construct(main_scene):
        main_scene.eqs=VGroup(MathTex(r"(1-x)y''-4xy'+5y=\cos(x)"),
                        MathTex(r"x\frac{d^3y}{dx^3}-\left(\frac{dy}{dx}\right)^4+y=0"),
                        MathTex(r"t^5y^{(4)}-t^3y''+6y=0"),
                        MathTex(r"\frac{d^2y}{dx^2}+\frac{dy}{dx}+y=\cos(r+u)"),
                        MathTex(r"\frac{d^2y}{dx^2}=\sqrt{1+\left(\frac{dy}{dx}\right)^2}"),
                        MathTex(r"\frac{d^2y}{dx^2}=-\frac{k}{y^2}"),
                        MathTex(r"\sin(\theta)y'''-\cos(\theta)y'=2"),
                        MathTex(r"y''-\left(1-\frac{y'^2}{3}\right)y'+y=0"),
                        MathTex(r"(y^2-1)dx+xdy=0")).arrange_in_grid(rows=3, cols=3, buff=(1, 1.5)).scale(0.7)

        with main_scene.voiceover(text="En este video vamos a comenzar una serie sobre ecuaciones diferenciales, en ella busco mostrar realmente la aplicación de esta rama de las matemáticas y dejar de ver estas expresiones solo como un tema complejo que tenemos <bookmark mark='A'/> que aprender más allá del cálculo diferencial e integral.") as tracker:
            main_scene.play(LaggedStart(*[Write(eq) for eq in main_scene.eqs], lag_ratio=0.4), run_time=tracker.time_until_bookmark('A'))
            main_scene.play(main_scene.eqs.animate.apply_complex_function(exp), run_time=tracker.get_remaining_duration())
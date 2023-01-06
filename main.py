'''
    Código para el video "¿Qué son las ecuaciones diferenciales?" de Paolo Inspires
    Copyright (C) 2022 por Paolo Alfonso Reyes Ramírez
'''

# Librerias
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.recorder import RecorderService
from sub_scenes.intro import Intro
from sub_scenes.que_son import QueSon
from sub_scenes.categorias import Categorias
from sub_scenes.tipos import Tipos
from sub_scenes.orden import Orden

# Configuración Global
config.background_color = WHITE
Text.set_default(color=BLACK)
Tex.set_default(color=BLACK)
MathTex.set_default(color=BLACK)

# Escena Principal
class Main(VoiceoverScene):
    def construct(main_scene):
        main_scene.set_speech_service(RecorderService())
        Intro.construct(main_scene)
        main_scene.wait()
        QueSon.construct(main_scene)
        main_scene.wait(0.5)
        Categorias.construct(main_scene)
        Tipos.construct(main_scene)
        Orden.construct(main_scene)
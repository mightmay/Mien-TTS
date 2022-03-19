#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import sys
import string
from argparse import RawTextHelpFormatter
# pylint: disable=redefined-outer-name, unused-argument
from pathlib import Path

# from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    if v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    raise argparse.ArgumentTypeError('Boolean value expected.')


def mainsynthesize(inputstring):
    print("Starting")

    # ts --text "Mv baac Saa mu en nyei dorn maiv zuotc ninh mbuo nyei die nyei nyungc zeiv zoux. Ninh mbuo kungx douh ganh duqv nyaanh hnangv, nyanc nyaanh hmuangx yaac mbienv baengh fim nyei leiz. Mv baac ninh mbuo gorngv.  Ninh oix zorqv meih mbuo gauh longx jiex nyei lingh deic caux a ngunc huingx caux ga lanv huingx jiu bun ninh nyei jien."     --model_path model/3k/model110000.pth.tar     --config_path model/3k/config.json

    # tts --text "Mv baac Saa mu en nyei dorn maiv zuotc ninh mbuo nyei die nyei nyungc zeiv zoux. Ninh mbuo kungx douh ganh duqv nyaanh hnangv, nyanc nyaanh hmuangx yaac mbienv baengh fim nyei leiz. Mv baac ninh mbuo gorngv.  Ninh oix zorqv meih mbuo gauh longx jiex nyei lingh deic caux a ngunc huingx caux ga lanv huingx jiu bun ninh nyei jien."     --model_path model/3k/best_model.pth.tar     --config_path model/3k/config.json

    # load model manager
    path = Path(__file__).parent / "../.models.json"
    #    manager = ModelManager(path)

    model_path = "model5k90k.pth.tar"
    config_path = "config5k90k.json"
    vocoder_path = None
    vocoder_config_path = None
    textInput = inputstring

    # RUN THE SYNTHESIS
    # load models
    synthesizer = Synthesizer(model_path, config_path, vocoder_path, vocoder_config_path, False)

    use_griffin_lim = vocoder_path is None
    print(" > Text: {}".format(textInput))

    # kick it
    wav = synthesizer.tts(textInput)
    import calendar
    import time
    ts = calendar.timegm(time.gmtime())
    #out_path = str(ts) + ".wav"
    out_path =  "voice.wav"
    # save the results

    print(" > Saving output to {}".format(out_path))
    synthesizer.save_wav(wav, out_path)


if __name__ == "__main__":
    print("running...")
    mainsynthesize()

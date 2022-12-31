from __future__ import absolute_import, division, print_function

from trainer_enc_lrl_hrl import Trainer
from options import MonodepthOptions

options = MonodepthOptions()
opts = options.parse()


if __name__ == "__main__":
    trainer = Trainer(opts)
    trainer.train()

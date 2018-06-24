YES = ('yes', 'y', 's', 'sim')
NO = ('no', 'n', 'nao')
YES_NO = {k: False if k in NO else True for k in YES + NO}

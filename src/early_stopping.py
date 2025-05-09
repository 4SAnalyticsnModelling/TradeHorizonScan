class EarlyStopping:
    def __init__(self, patience=50, delta=0):
        self.patience = patience
        self.delta = delta
        self.best_score = None
        self.early_stop = False
        self.counter = 0
        self.best_model_state = None
        self.is_this_best_so_far = False

    def __call__(self, val_loss, model, all_val_losses):
        score = -val_loss
        self.best_score = min(all_val_losses)
        if self.best_score is None:
            self.best_score = score
            self.best_model_state = model.state_dict()
        elif score < self.best_score + self.delta:
            self.counter += 1
            if self.counter >= self.patience:
                self.early_stop = True
        else:
            self.best_score = score
            self.best_model_state = model.state_dict()
            self.counter = 0
            self.is_this_best_so_far = True

    def load_best_model(self, model):
        model.load_state_dict(self.best_model_state)
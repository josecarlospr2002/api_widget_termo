class BloquesRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'bloques':
            return 'bbddt'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'bloques':
            return False
        return None

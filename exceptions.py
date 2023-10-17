class MissingConfigException(Exception):
  def __init__(self) -> None:
    self.message = "Keine Konfiguration für dieses Formular gefunden"
    super().__init__(self.message)

class DocumentTypeRecognitionException(Exception):
  def __init__(self) -> None:
    self.message = "Dokumentart nicht erkannt"
    super().__init__(self.message)

class FormException(Exception):
  def __init__(self) -> None:
    self.message = "Das Formular hat eine andere Stuktur als erwartet"
    super().__init__(self.message)

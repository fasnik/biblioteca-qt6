from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QWidget, QLineEdit
from PySide6.QtCore import Slot, Signal

from src.ui.ui_BibliotecaMainWindow import Ui_BibliotecaApp
from src.ui.ui_AddUser import Ui_Window as addUserDialog
from src.ui.ui_ListUsers import Ui_ListUsers
from src.ui.ui_AddPublication import Ui_AddPublication
from src.ui.ui_ListPublications import Ui_ListPublications
from src.ui.ui_RegisterCheckOut import Ui_RegisterChechOut
from src.ui.ui_ListCheckOut import Ui_ListCheckOut


from src.ui.table_model import TableModel

from src.models.biblio_models import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_BibliotecaApp()
        self.ui.setupUi(self)
        self.current_widget = None
        self.current_ui = None

        #Signals
        self.ui.actionAddUser.triggered.connect(self.ui_add_user)
        self.ui.actionQueryUser.triggered.connect(self.ui_query_users)
        self.ui.actionAddPublicacao.triggered.connect(self.ui_add_publication)
        self.ui.actionQueryPublicacao.triggered.connect(self.ui_query_publications)
        self.ui.actionregisterCheckOut.triggered.connect(self.ui_register_checkout)
        self.ui.actionregisterDevolucao.triggered.connect(self.ui_query_checkout)


    def build_ui(self, ui):
        a_ui = ui()
        a_ui.setupUi(self)
        self.current_ui = a_ui
        self.current_widget = self.current_ui.centralWidget
        self.takeCentralWidget()
        self.setCentralWidget(self.current_widget)
    
    # UIS
    @Slot()
    def ui_add_user(self):
        self.build_ui(addUserDialog)
        self.current_ui.confirm.released.connect(self.add_user)
    
    @Slot()
    def ui_add_publication(self):
        self.build_ui(Ui_AddPublication)
        self.current_ui.confirm.released.connect(self.add_publication)
    
    @Slot()
    def ui_register_checkout(self):
        self.build_ui(Ui_RegisterChechOut)
        self.current_ui.confirm.released.connect(self.register_checkout)
    
    @Slot()
    def ui_query_checkout(self):
        self.build_ui(Ui_ListCheckOut)
        self.current_ui.pesquisar.released.connect(self.get_checkout)
        
        #Loads All Users
        self.get_checkout()
    
    @Slot()
    def ui_query_users(self):
        self.build_ui(Ui_ListUsers)
        self.current_ui.pesquisar.released.connect(self.get_users)
        
        #Loads All Users
        self.get_users()
    
    @Slot()
    def ui_query_publications(self):
        self.build_ui(Ui_ListPublications)
        self.current_ui.pesquisar.released.connect(self.get_publications)
        
        #Loads All Users
        self.get_publications()
    
    #QUERIES
    @Slot()
    def add_user(self):
        new_user = Usuario()
        new_user.nome = self.current_ui.name.text()
        new_user.email = self.current_ui.email.text()
        new_user.telefone = self.current_ui.tel.text()

        try:
            new_user.save()
            txt = f"O usuário {self.current_ui.name.text()} foi adicionado."
        except:
            txt = f"Não foi possível adicionar o usuário."
        finally:
            # Avisa que a operação foi concluida
            alert = QDialog()
            alert.resize(300,100)
            alert_txt = QLabel(txt, alert)
            alert_txt.setWordWrap(True)
            alert_txt.setMargin(9)
            alert.exec()

    @Slot()
    def add_publication(self):
        new_publication = Publicacao()
        new_publication.nome = self.current_ui.name.text()
        new_publication.ano = self.current_ui.year.text()
        new_publication.autor = self.current_ui.author.text()
        new_publication.tema = self.current_ui.theme.text()

        try:
            new_publication.save()
            txt = f"A publicação {self.current_ui.name.text()} foi adicionada."
            for field in self.current_ui.centralWidget.findChildren(QLineEdit):
                field.clear()
        except Exception as e:
            txt = f"Não foi possível adicionar a publicação devido a \n {e}"
        finally:
            # Avisa que a operação foi concluida
            alert = QDialog()
            alert.resize(300,100)
            alert_txt = QLabel(txt, alert)
            alert_txt.setWordWrap(True)
            alert_txt.setMargin(9)
            alert.exec()
            
    
    @Slot()
    def register_checkout(self):
        new_checkout = Emprestimo()
        new_checkout.nome = self.current_ui.name.text()
        new_checkout.email = self.current_ui.email.text()
        new_checkout.telefone = self.current_ui.tel.text()

        try:
            new_checkout.save()
            txt = f"A publicação {self.current_ui.name.text()} foi adicionada."
        except:
            txt = f"Não foi possível adicionar a publicação."
        finally:
            # Avisa que a operação foi concluida
            alert = QDialog()
            alert.resize(300,100)
            alert_txt = QLabel(txt, alert)
            alert_txt.setWordWrap(True)
            alert_txt.setMargin(9)
            alert.exec()

    def return_checkout(self):
        new_checkout = Emprestimo()
        new_checkout.nome = self.current_ui.name.text()
        new_checkout.email = self.current_ui.email.text()
        new_checkout.telefone = self.current_ui.tel.text()

        try:
            new_checkout.save()
            txt = f"A publicação {self.current_ui.name.text()} foi adicionada."
        except:
            txt = f"Não foi possível adicionar a publicação."
        finally:
            # Avisa que a operação foi concluida
            alert = QDialog()
            alert.resize(300,100)
            alert_txt = QLabel(txt, alert)
            alert_txt.setWordWrap(True)
            alert_txt.setMargin(9)
            alert.exec()

    def get_users(self):
        search_param = self.current_ui.busca.text()
        query = Usuario.select(Usuario.nome, Usuario.email).where(Usuario.nome.contains(search_param)).dicts()
        users_list_dict: list[dict] = [row for row in query]

        if users_list_dict:
            users = TableModel(query)
            self.current_ui.mainWidget.setModel(users)

    def get_publications(self):
        search_param = self.current_ui.busca.text()
        query = Publicacao.select(Publicacao.nome, Publicacao.autor, Publicacao.ano).where(Publicacao.nome.contains(search_param)).dicts()
        users_list_dict: list[dict] = [row for row in query]

        if users_list_dict:
            publications = TableModel(query)
            self.current_ui.mainWidget.setModel(publications)
        else:
            dialog = QDialog()
            dialog.resize(300,100)
            QLabel("Nenhum item encontrado",dialog)
            dialog.exec()

    def get_checkout(self):
        search_param = self.current_ui.busca.text()
        query = Emprestimo.select(Emprestimo.id_usuario, Emprestimo.id_publicacao, Emprestimo.data_emprestimo).where(Emprestimo.id_usuario.contains(search_param)).dicts()
        users_list_dict: list[dict] = [row for row in query]

        if users_list_dict:
            checkout = TableModel(query)
            self.current_ui.mainWidget.setModel(checkout)

app = QApplication()
widget = MainWindow()
widget.show()
app.exec()

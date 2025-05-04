import unittest
from unittest.mock import patch, MagicMock
import io
import sys
from calculate.view import View

class TestView(unittest.TestCase):
    """Tests pour la classe View avec unittest."""

    def test_print_menu(self):
        """Test l'affichage du menu."""
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            View.print_menu()
            output = fake_out.getvalue()
            self.assertIn("Menu principal", output)
            self.assertIn("1. Addition", output)
            self.assertIn("34. Quitter", output)
    
    def test_print_error(self):
        """Test l'affichage des erreurs."""
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            View.print_error("Erreur de test")
            output = fake_out.getvalue()
            self.assertIn("Erreur", output)
            self.assertIn("Erreur de test", output)
    
    def test_get_user_input(self):
        """Test la récupération de l'entrée utilisateur."""
        with patch('builtins.input', return_value="test input"):
            result = View.get_user_input("Entrez une valeur: ")
            self.assertEqual(result, "test input")
    
    def test_print_result(self):
        """Test l'affichage du résultat."""
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            View.print_result("2+2", 4)
            output = fake_out.getvalue()
            self.assertIn("Résultat", output)
            self.assertIn("2+2", output)
            self.assertIn("4", output)
    
    def test_continue_message(self):
        """Test l'affichage du message de continuation."""
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            with patch('builtins.input', return_value=""):
                View.continue_message()
                output = fake_out.getvalue()
                self.assertIn("Appuyez sur Entrée pour continuer", output)

    def test_end_message(self):
        """Test l'affichage du message de fin."""
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            View.end_message()
            output = fake_out.getvalue()
            self.assertIn("Au revoir", output)
            self.assertIn("Merci d'avoir utilisé notre calculatrice", output)

    def test_print_welcome(self):
        """Test l'affichage du message de bienvenue."""
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            View.print_welcome()
            output = fake_out.getvalue()
            self.assertIn("Bienvenue", output)
            self.assertIn("Calculatrice Scientifique", output)

    def test_print_help(self):
        """Test l'affichage de l'aide générale."""
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            View.print_help()
            output = fake_out.getvalue()
            self.assertIn("Aide", output)
            self.assertIn("Commandes disponibles", output)

    def test_print_statistics_help(self):
        """Test l'affichage de l'aide pour les statistiques."""
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            View.print_statistics_help()
            output = fake_out.getvalue()
            self.assertIn("Aide Statistiques", output)
            self.assertIn("Fonctions statistiques disponibles", output)

    def test_print_visualization_help(self):
        """Test l'affichage de l'aide pour la visualisation."""
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            View.print_visualization_help()
            output = fake_out.getvalue()
            self.assertIn("Aide Visualisation", output)
            self.assertIn("Fonctions de visualisation disponibles", output)

    def test_handle_message_errors(self):
        """Test la gestion des erreurs pour les méthodes d'affichage."""
        # Test avec des erreurs
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            with patch('builtins.print', side_effect=Exception("Erreur simulée")):
                # Le test vérifie simplement que l'exception est capturée et ne propage pas
                result = View.print_error("Test")
                self.assertIsNone(result)
                
                result = View.print_menu()
                self.assertIsNone(result)
                
                result = View.print_result("test", "result")
                self.assertIsNone(result)
                
                result = View.print_welcome()
                self.assertIsNone(result)
                
                result = View.print_help()
                self.assertIsNone(result)
                
                result = View.print_statistics_help()
                self.assertIsNone(result)
                
                result = View.print_visualization_help()
                self.assertIsNone(result)
                
                result = View.end_message()
                self.assertIsNone(result)

    def test_get_user_input_error(self):
        """Test la gestion des erreurs pour get_user_input."""
        with patch('builtins.input', side_effect=Exception("Erreur simulée")):
            result = View.get_user_input("Test: ")
            self.assertEqual(result, "")

    def test_continue_message_error(self):
        """Test la gestion des erreurs pour continue_message."""
        with patch('builtins.input', side_effect=Exception("Erreur simulée")):
            result = View.continue_message()
            self.assertIsNone(result)

    def test_print_result_none(self):
        """Test l'affichage du résultat quand il est None."""
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            View.print_result("operation", None)
            output = fake_out.getvalue()
            self.assertIn("Résultat", output)
            self.assertIn("operation", output)
            self.assertIn("None", output)


if __name__ == '__main__':
    unittest.main() 
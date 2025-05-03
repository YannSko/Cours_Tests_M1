import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from calculate.view import View

class TestView(unittest.TestCase):
    """Tests pour la classe View avec unittest."""

    def test_print_menu(self):
        """Test l'affichage du menu."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            View.print_menu()
            output = fake_out.getvalue()
            self.assertIn("=== Calculatrice Scientifique ===", output)
            self.assertIn("Opérations de base:", output)
            self.assertIn("Statistiques:", output)
            self.assertIn("Visualisation:", output)
            self.assertIn("Autres:", output)

    def test_print_menu_error(self):
        """Test la gestion d'erreur du menu."""
        with patch('builtins.print', side_effect=Exception("Erreur d'affichage")):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                View.print_menu()
                self.assertIn("Erreur lors de l'affichage du menu", fake_out.getvalue())

    def test_get_user_input(self):
        """Test la récupération de l'entrée utilisateur."""
        with patch('builtins.input', return_value="test"):
            result = View.get_user_input("Entrez une valeur")
            self.assertEqual(result, "test")

    def test_get_user_input_empty(self):
        """Test la récupération d'une entrée vide."""
        with patch('builtins.input', return_value=""):
            result = View.get_user_input("Entrez une valeur")
            self.assertEqual(result, "")

    def test_get_user_input_error(self):
        """Test la gestion d'erreur de l'entrée utilisateur."""
        with patch('builtins.input', side_effect=Exception("Erreur d'entrée")):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                result = View.get_user_input("Entrez une valeur")
                self.assertIn("Erreur lors de la récupération de l'entrée", fake_out.getvalue())
                self.assertEqual(result, "")

    def test_get_user_input_invalid_message(self):
        """Test l'entrée avec un message invalide."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            result = View.get_user_input(123)
            self.assertIn("Erreur lors de la récupération de l'entrée", fake_out.getvalue())
            self.assertEqual(result, "")

    def test_print_result(self):
        """Test l'affichage du résultat."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            View.print_result("2 + 3", 5)
            self.assertIn("Résultat de 2 + 3 = 5", fake_out.getvalue())

    def test_print_result_none(self):
        """Test l'affichage d'un résultat None."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            View.print_result("test", None)
            self.assertIn("Erreur lors de l'affichage du résultat", fake_out.getvalue())

    def test_print_result_error(self):
        """Test la gestion d'erreur de l'affichage du résultat."""
        with patch('builtins.print', side_effect=Exception("Erreur d'affichage")):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                View.print_result("test", 5)
                self.assertIn("Erreur lors de l'affichage du résultat", fake_out.getvalue())

    def test_continue_message(self):
        """Test le message de continuation."""
        with patch('builtins.input', return_value=""):
            View.continue_message()
            # Pas besoin d'assertion, on vérifie juste que ça ne lève pas d'exception

    def test_continue_message_error(self):
        """Test la gestion d'erreur du message de continuation."""
        with patch('builtins.input', side_effect=Exception("Erreur d'entrée")):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                View.continue_message()
                self.assertIn("Erreur lors de l'affichage du message de continuation", fake_out.getvalue())

    def test_end_message(self):
        """Test le message de fin."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            View.end_message()
            self.assertIn("Merci d'avoir utilisé la calculatrice scientifique!", fake_out.getvalue())

    def test_end_message_error(self):
        """Test la gestion d'erreur du message de fin."""
        with patch('builtins.print', side_effect=Exception("Erreur d'affichage")):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                View.end_message()
                self.assertIn("Erreur lors de l'affichage du message de fin", fake_out.getvalue())

    def test_print_visualization_help(self):
        """Test l'aide pour les visualisations."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            View.print_visualization_help()
            output = fake_out.getvalue()
            self.assertIn("=== Aide pour les visualisations ===", output)
            self.assertIn("Tracer une fonction:", output)
            self.assertIn("Nuage de points:", output)
            self.assertIn("Histogramme:", output)
            self.assertIn("Graphique polaire:", output)
            self.assertIn("Graphique 3D:", output)
            self.assertIn("Boxplot:", output)
            self.assertIn("Graphique Q-Q:", output)
            self.assertIn("Heatmap:", output)
            self.assertIn("Graphique en camembert:", output)
            self.assertIn("Graphique en barres:", output)

    def test_print_visualization_help_error(self):
        """Test la gestion d'erreur de l'aide pour les visualisations."""
        with patch('builtins.print', side_effect=Exception("Erreur d'affichage")):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                View.print_visualization_help()
                self.assertIn("Erreur lors de l'affichage de l'aide", fake_out.getvalue())

    def test_print_error(self):
        """Test l'affichage d'un message d'erreur."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            View.print_error("Test d'erreur")
            self.assertIn("Erreur: Test d'erreur", fake_out.getvalue())

    def test_print_error_invalid_message(self):
        """Test l'affichage d'un message d'erreur invalide."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            View.print_error(123)
            self.assertIn("Erreur lors de l'affichage du message d'erreur", fake_out.getvalue())

    def test_print_error_error(self):
        """Test la gestion d'erreur de l'affichage d'erreur."""
        with patch('builtins.print', side_effect=Exception("Erreur d'affichage")):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                View.print_error("Test d'erreur")
                self.assertIn("Erreur lors de l'affichage du message d'erreur", fake_out.getvalue())

    def test_print_welcome(self):
        """Test le message de bienvenue."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            View.print_welcome()
            output = fake_out.getvalue()
            self.assertIn("=== Bienvenue dans la Calculatrice Scientifique ===", output)
            self.assertIn("Cette calculatrice vous permet d'effectuer des opérations mathématiques", output)
            self.assertIn("de base, des calculs statistiques et de créer des visualisations.", output)

    def test_print_welcome_error(self):
        """Test la gestion d'erreur du message de bienvenue."""
        with patch('builtins.print', side_effect=Exception("Erreur d'affichage")):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                View.print_welcome()
                self.assertIn("Erreur lors de l'affichage du message de bienvenue", fake_out.getvalue())

    def test_print_help(self):
        """Test l'aide générale."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            View.print_help()
            output = fake_out.getvalue()
            self.assertIn("=== Aide Générale ===", output)
            self.assertIn("Pour utiliser la calculatrice:", output)
            self.assertIn("1. Choisissez une opération dans le menu", output)
            self.assertIn("2. Entrez les valeurs requises", output)
            self.assertIn("3. Consultez le résultat", output)
            self.assertIn("4. Continuez avec d'autres opérations ou quittez", output)
            self.assertIn("Notes importantes:", output)
            self.assertIn("- Utilisez des points pour les nombres décimaux", output)
            self.assertIn("- Séparez les valeurs par des virgules pour les listes", output)
            self.assertIn("- Utilisez des points-virgules pour séparer les listes", output)
            self.assertIn("- Consultez l'aide spécifique pour les visualisations", output)

    def test_print_help_error(self):
        """Test la gestion d'erreur de l'aide générale."""
        with patch('builtins.print', side_effect=Exception("Erreur d'affichage")):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                View.print_help()
                self.assertIn("Erreur lors de l'affichage de l'aide générale", fake_out.getvalue())

    def test_print_statistics_help(self):
        """Test l'aide pour les fonctions statistiques."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            View.print_statistics_help()
            output = fake_out.getvalue()
            self.assertIn("=== Aide pour les Fonctions Statistiques ===", output)
            self.assertIn("Moyenne:", output)
            self.assertIn("Médiane:", output)
            self.assertIn("Mode:", output)
            self.assertIn("Écart-type:", output)
            self.assertIn("Variance:", output)
            self.assertIn("Percentile:", output)
            self.assertIn("Corrélation:", output)
            self.assertIn("Régression linéaire:", output)

    def test_print_statistics_help_error(self):
        """Test la gestion d'erreur de l'aide statistique."""
        with patch('builtins.print', side_effect=Exception("Erreur d'affichage")):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                View.print_statistics_help()
                self.assertIn("Erreur lors de l'affichage de l'aide statistique", fake_out.getvalue())

    def test_all_print_methods_exist(self):
        """Test que toutes les méthodes d'affichage existent."""
        methods = [attr for attr in dir(View) if callable(getattr(View, attr)) and not attr.startswith("_")]
        expected_methods = [
            "print_menu", "get_user_input", "print_result", "continue_message", 
            "end_message", "print_visualization_help", "print_error", 
            "print_welcome", "print_help", "print_statistics_help"
        ]
        for method in expected_methods:
            self.assertIn(method, methods, f"La méthode {method} n'existe pas dans la classe View")
            
    def test_get_user_input_formatting(self):
        """Test le formatage de l'entrée utilisateur."""
        with patch('builtins.input', return_value="  test  "):
            result = View.get_user_input("Message")
            self.assertEqual(result, "test")  # Vérifie que les espaces sont supprimés
            
    def test_print_result_formatting(self):
        """Test le formatage du résultat."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            View.print_result("2 + 3", 5.000)
            self.assertIn("Résultat de 2 + 3 = 5.0", fake_out.getvalue())
            
            fake_out.truncate(0)
            fake_out.seek(0)
            
            View.print_result("liste", [1, 2, 3])
            self.assertIn("Résultat de liste = [1, 2, 3]", fake_out.getvalue())


if __name__ == '__main__':
    unittest.main() 
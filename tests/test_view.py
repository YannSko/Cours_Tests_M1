import pytest
from unittest.mock import patch, MagicMock
from calculate.view import View

class TestView:
    """Tests pour le module View."""

    @patch('builtins.print')
    def test_print_menu(self, mock_print):
        """Test de l'affichage du menu."""
        View.print_menu()
        assert mock_print.call_count > 0
        # Vérifie que le menu contient les sections principales
        menu_text = ' '.join(str(call) for call in mock_print.call_args_list)
        assert "Opérations de base" in menu_text
        assert "Statistiques" in menu_text
        assert "Visualisation" in menu_text

    @patch('builtins.input')
    def test_get_user_input(self, mock_input):
        """Test de la récupération de l'entrée utilisateur."""
        # Test avec une entrée normale
        mock_input.return_value = "2 + 3"
        result = View.get_user_input("Entrez votre opération")
        assert result == "2 + 3"
        assert mock_input.call_count == 1

        # Test avec une entrée vide
        mock_input.return_value = ""
        result = View.get_user_input("Entrez votre opération")
        assert result == ""
        assert mock_input.call_count == 2

        # Test avec des caractères spéciaux
        mock_input.return_value = "2 + 3!"
        result = View.get_user_input("Entrez votre opération")
        assert result == "2 + 3!"
        assert mock_input.call_count == 3

    @patch('builtins.print')
    def test_print_result(self, mock_print):
        """Test de l'affichage du résultat."""
        # Test avec un résultat numérique
        View.print_result("2 + 3", 5)
        assert mock_print.call_count == 1
        assert "2 + 3 = 5" in str(mock_print.call_args)

        # Test avec un résultat de type dict (pour la régression linéaire)
        result_dict = {'slope': 2.0, 'intercept': 1.0, 'r_squared': 0.95}
        View.print_result("regression(1,2,3;4,5,6)", result_dict)
        assert "Pente" in str(mock_print.call_args)
        assert "Ordonnée à l'origine" in str(mock_print.call_args)
        assert "R²" in str(mock_print.call_args)

        # Test avec un résultat de type str (pour les visualisations)
        View.print_result("plot(x^2)", "Graphique sauvegardé")
        assert "Graphique sauvegardé" in str(mock_print.call_args)

    @patch('builtins.print')
    def test_continue_message(self, mock_print):
        """Test du message de continuation."""
        View.continue_message()
        assert mock_print.call_count == 1
        assert "Appuyez sur Entrée pour continuer" in str(mock_print.call_args)

    @patch('builtins.print')
    def test_end_message(self, mock_print):
        """Test du message de fin."""
        View.end_message()
        assert mock_print.call_count == 1
        assert "Au revoir" in str(mock_print.call_args)

    @patch('builtins.print')
    def test_print_visualization_help(self, mock_print):
        """Test de l'aide pour les visualisations."""
        View.print_visualization_help()
        assert mock_print.call_count > 0
        help_text = ' '.join(str(call) for call in mock_print.call_args_list)
        assert "Exemples de commandes" in help_text
        assert "plot" in help_text
        assert "scatter" in help_text
        assert "histogram" in help_text
        assert "polar" in help_text
        assert "3d" in help_text
        assert "boxplot" in help_text
        assert "qqplot" in help_text
        assert "heatmap" in help_text
        assert "pie" in help_text
        assert "bar" in help_text

    @patch('builtins.print')
    def test_print_error(self, mock_print):
        """Test de l'affichage des erreurs."""
        # Test avec une erreur de division par zéro
        View.print_error("Division par zéro")
        assert mock_print.call_count == 1
        assert "Erreur" in str(mock_print.call_args)
        assert "Division par zéro" in str(mock_print.call_args)

        # Test avec une erreur de syntaxe
        View.print_error("Syntaxe invalide")
        assert mock_print.call_count == 2
        assert "Erreur" in str(mock_print.call_args)
        assert "Syntaxe invalide" in str(mock_print.call_args)

    @patch('builtins.print')
    def test_print_welcome(self, mock_print):
        """Test du message de bienvenue."""
        View.print_welcome()
        assert mock_print.call_count == 1
        assert "Bienvenue" in str(mock_print.call_args)

    @patch('builtins.print')
    def test_print_help(self, mock_print):
        """Test de l'aide générale."""
        View.print_help()
        assert mock_print.call_count > 0
        help_text = ' '.join(str(call) for call in mock_print.call_args_list)
        assert "Aide" in help_text
        assert "Opérations disponibles" in help_text

    @patch('builtins.print')
    def test_print_statistics_help(self, mock_print):
        """Test de l'aide pour les statistiques."""
        View.print_statistics_help()
        assert mock_print.call_count > 0
        help_text = ' '.join(str(call) for call in mock_print.call_args_list)
        assert "Statistiques" in help_text
        assert "mean" in help_text
        assert "median" in help_text
        assert "mode" in help_text
        assert "std" in help_text
        assert "var" in help_text
        assert "percentile" in help_text
        assert "correlation" in help_text
        assert "regression" in help_text 
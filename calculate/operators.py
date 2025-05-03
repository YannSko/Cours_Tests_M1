import math
import re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from scipy import stats

class Operators:
    def __init__(self):
        self.operators = {
            '+': self.addition,
            '-': self.substraction,
            '*': self.multiplication,
            '/': self.division,
            '^': self.power,
            'sqrt': self.square_root,
            'log': self.logarithm,
            '%': self.modulo,
            'sin': self.sine,
            'cos': self.cosine,
            'tan': self.tangent,
            '!': self.factorial,
            'abs': self.absolute,
            'exp': self.exponential,
            'mean': self.mean,
            'median': self.median,
            'mode': self.mode,
            'std': self.standard_deviation,
            'var': self.variance,
            'percentile': self.percentile,
            'correlation': self.correlation,
            'regression': self.linear_regression
        }
        self.visualization_functions = {
            'plot': self.plot_function,
            'scatter': self.scatter_plot,
            'histogram': self.histogram,
            'polar': self.polar_plot,
            '3d': self.plot_3d,
            'boxplot': self.boxplot,
            'qqplot': self.qqplot,
            'heatmap': self.heatmap,
            'pie': self.pie_chart,
            'bar': self.bar_chart
        }

    def addition(self, operation):
        """Addition de deux nombres"""
        a, b = self._parse_operation(operation, '+')
        return a + b

    def substraction(self, operation):
        """Soustraction de deux nombres"""
        a, b = self._parse_operation(operation, '-')
        return a - b

    def multiplication(self, operation):
        """Multiplication de deux nombres"""
        a, b = self._parse_operation(operation, '*')
        return a * b

    def division(self, operation):
        """Division de deux nombres"""
        a, b = self._parse_operation(operation, '/')
        if b == 0:
            raise ValueError("Division par zéro impossible")
        return a / b

    def power(self, operation):
        """Calcul de la puissance"""
        a, b = self._parse_operation(operation, '^')
        return math.pow(a, b)

    def square_root(self, operation):
        """Calcul de la racine carrée"""
        a = self._parse_single_number(operation, 'sqrt')
        if a < 0:
            raise ValueError("Impossible de calculer la racine carrée d'un nombre négatif")
        return math.sqrt(a)

    def logarithm(self, operation):
        """Calcul du logarithme naturel"""
        a = self._parse_single_number(operation, 'log')
        if a <= 0:
            raise ValueError("Le logarithme n'est défini que pour les nombres strictement positifs")
        return math.log(a)

    def modulo(self, operation):
        """Calcul du modulo"""
        a, b = self._parse_operation(operation, '%')
        if b == 0:
            raise ValueError("Division par zéro impossible")
        return a % b

    def sine(self, operation):
        """Calcul du sinus (en radians)"""
        a = self._parse_single_number(operation, 'sin')
        return math.sin(a)

    def cosine(self, operation):
        """Calcul du cosinus (en radians)"""
        a = self._parse_single_number(operation, 'cos')
        return math.cos(a)

    def tangent(self, operation):
        """Calcul de la tangente (en radians)"""
        a = self._parse_single_number(operation, 'tan')
        return math.tan(a)

    def factorial(self, operation):
        """Calcul de la factorielle"""
        a = self._parse_single_number(operation, '!')
        if not a.is_integer() or a < 0:
            raise ValueError("La factorielle n'est définie que pour les entiers positifs")
        return math.factorial(int(a))

    def absolute(self, operation):
        """Calcul de la valeur absolue"""
        a = self._parse_single_number(operation, 'abs')
        return abs(a)

    def exponential(self, operation):
        """Calcul de l'exponentielle"""
        a = self._parse_single_number(operation, 'exp')
        return math.exp(a)

    def mean(self, operation):
        """Calcule la moyenne d'une série de nombres"""
        values = self._parse_list(operation, 'mean')
        return np.mean(values)

    def median(self, operation):
        """Calcule la médiane d'une série de nombres"""
        values = self._parse_list(operation, 'median')
        return np.median(values)

    def mode(self, operation):
        """Calcule le mode d'une série de nombres"""
        values = self._parse_list(operation, 'mode')
        return stats.mode(values)[0][0]

    def standard_deviation(self, operation):
        """Calcule l'écart-type d'une série de nombres"""
        values = self._parse_list(operation, 'std')
        return np.std(values)

    def variance(self, operation):
        """Calcule la variance d'une série de nombres"""
        values = self._parse_list(operation, 'var')
        return np.var(values)

    def percentile(self, operation):
        """Calcule le percentile d'une série de nombres"""
        parts = self._parse_operation_with_percentile(operation, 'percentile')
        values = parts[0]
        p = parts[1]
        return np.percentile(values, p)

    def correlation(self, operation):
        """Calcule le coefficient de corrélation entre deux séries"""
        x, y = self._parse_two_lists(operation, 'correlation')
        return np.corrcoef(x, y)[0,1]

    def linear_regression(self, operation):
        """Effectue une régression linéaire sur deux séries de données"""
        x, y = self._parse_two_lists(operation, 'regression')
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        return {
            'slope': slope,
            'intercept': intercept,
            'r_squared': r_value**2,
            'p_value': p_value
        }

    def _parse_operation(self, operation, operator):
        """Parse une opération binaire"""
        try:
            parts = operation.split(operator)
            if len(parts) != 2:
                raise ValueError(f"Format d'opération invalide pour {operator}")
            return float(parts[0].strip()), float(parts[1].strip())
        except ValueError as e:
            raise ValueError(f"Format de nombre invalide: {str(e)}")

    def _parse_single_number(self, operation, operator):
        """Parse une opération unaire"""
        try:
            # Supprime l'opérateur et les parenthèses si présentes
            number_str = operation.replace(operator, '').strip()
            number_str = number_str.strip('()')
            return float(number_str)
        except ValueError as e:
            raise ValueError(f"Format de nombre invalide: {str(e)}")

    def evaluate(self, operation):
        """Évalue une expression mathématique"""
        # Nettoie l'opération
        operation = operation.strip()
        
        # Vérifie si c'est une opération unaire
        for op in ['sqrt', 'log', 'sin', 'cos', 'tan', 'abs', 'exp']:
            if operation.startswith(op):
                return self.operators[op](operation)
        
        # Vérifie si c'est une factorielle
        if operation.endswith('!'):
            return self.factorial(operation)
        
        # Pour les opérations binaires
        for op in ['+', '-', '*', '/', '^', '%']:
            if op in operation:
                return self.operators[op](operation)
        
        raise ValueError("Opération non reconnue")

    def plot_function(self, operation):
        """
        Trace le graphe d'une fonction mathématique.
        Format: plot(f(x), x_min, x_max)
        Exemple: plot(x^2, -10, 10)
        """
        try:
            # Parse l'expression de la fonction et les limites
            parts = operation.replace('plot(', '').replace(')', '').split(',')
            if len(parts) != 3:
                raise ValueError("Format invalide. Utilisez: plot(f(x), x_min, x_max)")
            
            expr = parts[0].strip()
            x_min = float(parts[1].strip())
            x_max = float(parts[2].strip())
            
            # Créer les points x
            x = np.linspace(x_min, x_max, 1000)
            
            # Évaluer la fonction pour chaque point x
            y = []
            for x_val in x:
                # Remplacer x par la valeur actuelle dans l'expression
                expr_eval = expr.replace('x', str(x_val))
                try:
                    y_val = eval(expr_eval)
                    y.append(y_val)
                except:
                    y.append(np.nan)
            
            # Créer le graphique
            fig = Figure(figsize=(10, 6))
            canvas = FigureCanvasAgg(fig)
            ax = fig.add_subplot(111)
            
            ax.plot(x, y)
            ax.grid(True)
            ax.set_title(f'Graphe de {expr}')
            ax.set_xlabel('x')
            ax.set_ylabel('f(x)')
            
            # Sauvegarder le graphique
            fig.savefig('function_plot.png')
            return "Graphique sauvegardé dans 'function_plot.png'"
            
        except Exception as e:
            raise ValueError(f"Erreur lors du tracé: {str(e)}")

    def scatter_plot(self, operation):
        """
        Crée un nuage de points.
        Format: scatter(x1,y1,x2,y2,...)
        """
        try:
            # Parse les coordonnées
            coords = operation.replace('scatter(', '').replace(')', '').split(',')
            if len(coords) % 2 != 0:
                raise ValueError("Nombre impair de coordonnées")
            
            x = [float(coords[i]) for i in range(0, len(coords), 2)]
            y = [float(coords[i+1]) for i in range(0, len(coords), 2)]
            
            # Créer le graphique
            fig = Figure(figsize=(10, 6))
            canvas = FigureCanvasAgg(fig)
            ax = fig.add_subplot(111)
            
            ax.scatter(x, y)
            ax.grid(True)
            ax.set_title('Nuage de points')
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            
            fig.savefig('scatter_plot.png')
            return "Graphique sauvegardé dans 'scatter_plot.png'"
            
        except Exception as e:
            raise ValueError(f"Erreur lors du tracé: {str(e)}")

    def histogram(self, operation):
        """
        Crée un histogramme.
        Format: histogram(valeur1,valeur2,...)
        """
        try:
            # Parse les valeurs
            values = [float(x.strip()) for x in operation.replace('histogram(', '').replace(')', '').split(',')]
            
            # Créer le graphique
            fig = Figure(figsize=(10, 6))
            canvas = FigureCanvasAgg(fig)
            ax = fig.add_subplot(111)
            
            ax.hist(values, bins='auto')
            ax.grid(True)
            ax.set_title('Histogramme')
            ax.set_xlabel('Valeurs')
            ax.set_ylabel('Fréquence')
            
            fig.savefig('histogram.png')
            return "Graphique sauvegardé dans 'histogram.png'"
            
        except Exception as e:
            raise ValueError(f"Erreur lors du tracé: {str(e)}")

    def polar_plot(self, operation):
        """
        Crée un graphique polaire.
        Format: polar(r(theta), theta_min, theta_max)
        """
        try:
            # Parse l'expression et les limites
            parts = operation.replace('polar(', '').replace(')', '').split(',')
            if len(parts) != 3:
                raise ValueError("Format invalide. Utilisez: polar(r(theta), theta_min, theta_max)")
            
            expr = parts[0].strip()
            theta_min = float(parts[1].strip())
            theta_max = float(parts[2].strip())
            
            # Créer les points theta
            theta = np.linspace(theta_min, theta_max, 1000)
            
            # Évaluer la fonction pour chaque point theta
            r = []
            for theta_val in theta:
                expr_eval = expr.replace('theta', str(theta_val))
                try:
                    r_val = eval(expr_eval)
                    r.append(r_val)
                except:
                    r.append(np.nan)
            
            # Créer le graphique
            fig = Figure(figsize=(10, 10))
            canvas = FigureCanvasAgg(fig)
            ax = fig.add_subplot(111, projection='polar')
            
            ax.plot(theta, r)
            ax.grid(True)
            ax.set_title(f'Graphique polaire de {expr}')
            
            fig.savefig('polar_plot.png')
            return "Graphique sauvegardé dans 'polar_plot.png'"
            
        except Exception as e:
            raise ValueError(f"Erreur lors du tracé: {str(e)}")

    def plot_3d(self, operation):
        """
        Crée un graphique 3D.
        Format: 3d(z(x,y), x_min, x_max, y_min, y_max)
        """
        try:
            # Parse l'expression et les limites
            parts = operation.replace('3d(', '').replace(')', '').split(',')
            if len(parts) != 5:
                raise ValueError("Format invalide. Utilisez: 3d(z(x,y), x_min, x_max, y_min, y_max)")
            
            expr = parts[0].strip()
            x_min = float(parts[1].strip())
            x_max = float(parts[2].strip())
            y_min = float(parts[3].strip())
            y_max = float(parts[4].strip())
            
            # Créer la grille
            x = np.linspace(x_min, x_max, 100)
            y = np.linspace(y_min, y_max, 100)
            X, Y = np.meshgrid(x, y)
            
            # Évaluer la fonction
            Z = np.zeros_like(X)
            for i in range(len(x)):
                for j in range(len(y)):
                    expr_eval = expr.replace('x', str(X[i,j])).replace('y', str(Y[i,j]))
                    try:
                        Z[i,j] = eval(expr_eval)
                    except:
                        Z[i,j] = np.nan
            
            # Créer le graphique
            fig = Figure(figsize=(10, 8))
            canvas = FigureCanvasAgg(fig)
            ax = fig.add_subplot(111, projection='3d')
            
            ax.plot_surface(X, Y, Z, cmap='viridis')
            ax.set_title(f'Surface 3D de {expr}')
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_zlabel('z')
            
            fig.savefig('3d_plot.png')
            return "Graphique sauvegardé dans '3d_plot.png'"
            
        except Exception as e:
            raise ValueError(f"Erreur lors du tracé: {str(e)}")

    def boxplot(self, operation):
        """Crée un diagramme en boîte (boxplot)"""
        try:
            values = self._parse_list(operation, 'boxplot')
            
            fig = Figure(figsize=(10, 6))
            canvas = FigureCanvasAgg(fig)
            ax = fig.add_subplot(111)
            
            ax.boxplot(values)
            ax.set_title('Diagramme en boîte')
            ax.set_ylabel('Valeurs')
            
            fig.savefig('boxplot.png')
            return "Graphique sauvegardé dans 'boxplot.png'"
        except Exception as e:
            raise ValueError(f"Erreur lors du tracé: {str(e)}")

    def qqplot(self, operation):
        """Crée un graphique Q-Q (quantile-quantile)"""
        try:
            values = self._parse_list(operation, 'qqplot')
            
            fig = Figure(figsize=(10, 6))
            canvas = FigureCanvasAgg(fig)
            ax = fig.add_subplot(111)
            
            stats.probplot(values, dist="norm", plot=ax)
            ax.set_title('Graphique Q-Q')
            
            fig.savefig('qqplot.png')
            return "Graphique sauvegardé dans 'qqplot.png'"
        except Exception as e:
            raise ValueError(f"Erreur lors du tracé: {str(e)}")

    def heatmap(self, operation):
        """Crée une carte de chaleur (heatmap)"""
        try:
            matrix = self._parse_matrix(operation, 'heatmap')
            
            fig = Figure(figsize=(10, 8))
            canvas = FigureCanvasAgg(fig)
            ax = fig.add_subplot(111)
            
            im = ax.imshow(matrix, cmap='viridis')
            fig.colorbar(im)
            ax.set_title('Carte de chaleur')
            
            fig.savefig('heatmap.png')
            return "Graphique sauvegardé dans 'heatmap.png'"
        except Exception as e:
            raise ValueError(f"Erreur lors du tracé: {str(e)}")

    def pie_chart(self, operation):
        """Crée un diagramme circulaire"""
        try:
            values, labels = self._parse_pie_data(operation)
            
            fig = Figure(figsize=(10, 8))
            canvas = FigureCanvasAgg(fig)
            ax = fig.add_subplot(111)
            
            ax.pie(values, labels=labels, autopct='%1.1f%%')
            ax.set_title('Diagramme circulaire')
            
            fig.savefig('pie_chart.png')
            return "Graphique sauvegardé dans 'pie_chart.png'"
        except Exception as e:
            raise ValueError(f"Erreur lors du tracé: {str(e)}")

    def bar_chart(self, operation):
        """Crée un diagramme en barres"""
        try:
            values, labels = self._parse_bar_data(operation)
            
            fig = Figure(figsize=(10, 6))
            canvas = FigureCanvasAgg(fig)
            ax = fig.add_subplot(111)
            
            ax.bar(labels, values)
            ax.set_title('Diagramme en barres')
            plt.xticks(rotation=45)
            
            fig.savefig('bar_chart.png')
            return "Graphique sauvegardé dans 'bar_chart.png'"
        except Exception as e:
            raise ValueError(f"Erreur lors du tracé: {str(e)}")

    def _parse_list(self, operation, operator):
        """Parse une liste de nombres"""
        try:
            values_str = operation.replace(f'{operator}(', '').replace(')', '')
            return [float(x.strip()) for x in values_str.split(',')]
        except ValueError as e:
            raise ValueError(f"Format de liste invalide: {str(e)}")

    def _parse_two_lists(self, operation, operator):
        """Parse deux listes de nombres"""
        try:
            parts = operation.replace(f'{operator}(', '').replace(')', '').split(';')
            if len(parts) != 2:
                raise ValueError("Format invalide. Utilisez: operator(liste1;liste2)")
            return self._parse_list(parts[0], ''), self._parse_list(parts[1], '')
        except ValueError as e:
            raise ValueError(f"Format de liste invalide: {str(e)}")

    def _parse_matrix(self, operation, operator):
        """Parse une matrice de nombres"""
        try:
            matrix_str = operation.replace(f'{operator}(', '').replace(')', '')
            rows = matrix_str.split(';')
            return np.array([self._parse_list(row, '') for row in rows])
        except ValueError as e:
            raise ValueError(f"Format de matrice invalide: {str(e)}")

    def _parse_pie_data(self, operation):
        """Parse les données pour un diagramme circulaire"""
        try:
            data_str = operation.replace('pie(', '').replace(')', '')
            parts = data_str.split(';')
            if len(parts) != 2:
                raise ValueError("Format invalide. Utilisez: pie(valeurs;labels)")
            values = self._parse_list(parts[0], '')
            labels = [x.strip() for x in parts[1].split(',')]
            if len(values) != len(labels):
                raise ValueError("Le nombre de valeurs doit correspondre au nombre de labels")
            return values, labels
        except ValueError as e:
            raise ValueError(f"Format de données invalide: {str(e)}")

    def _parse_bar_data(self, operation):
        """Parse les données pour un diagramme en barres"""
        try:
            data_str = operation.replace('bar(', '').replace(')', '')
            parts = data_str.split(';')
            if len(parts) != 2:
                raise ValueError("Format invalide. Utilisez: bar(valeurs;labels)")
            values = self._parse_list(parts[0], '')
            labels = [x.strip() for x in parts[1].split(',')]
            if len(values) != len(labels):
                raise ValueError("Le nombre de valeurs doit correspondre au nombre de labels")
            return values, labels
        except ValueError as e:
            raise ValueError(f"Format de données invalide: {str(e)}")

    def _parse_operation_with_percentile(self, operation, operator):
        """Parse une opération avec un percentile"""
        try:
            parts = operation.replace(f'{operator}(', '').replace(')', '').split(';')
            if len(parts) != 2:
                raise ValueError("Format invalide. Utilisez: operator(valeurs;percentile)")
            values = self._parse_list(parts[0], '')
            p = float(parts[1].strip())
            if not 0 <= p <= 100:
                raise ValueError("Le percentile doit être entre 0 et 100")
            return values, p
        except ValueError as e:
            raise ValueError(f"Format invalide: {str(e)}")

    def visualize(self, operation):
        """
        Méthode principale pour la visualisation qui détermine le type de graphique à créer
        """
        operation = operation.strip()
        
        # Déterminer le type de visualisation
        for viz_type, func in self.visualization_functions.items():
            if operation.startswith(viz_type):
                return func(operation)
        
        raise ValueError("Type de visualisation non reconnu") 
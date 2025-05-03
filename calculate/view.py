class View:
    @staticmethod
    def print_menu():
        """Affiche le menu principal de la calculatrice"""
        print("\n=== Calculatrice Scientifique ===")
        print("\nOpérations de base:")
        print("1. Addition (+)")
        print("2. Soustraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Puissance (^)")
        print("6. Racine carrée (sqrt)")
        print("7. Logarithme (log)")
        print("8. Modulo (%)")
        print("9. Sinus (sin)")
        print("10. Cosinus (cos)")
        print("11. Tangente (tan)")
        print("12. Factorielle (!)")
        print("13. Valeur absolue (abs)")
        print("14. Exponentielle (exp)")
        
        print("\nStatistiques:")
        print("15. Moyenne (mean)")
        print("16. Médiane (median)")
        print("17. Mode (mode)")
        print("18. Écart-type (std)")
        print("19. Variance (var)")
        print("20. Percentile (percentile)")
        print("21. Corrélation (correlation)")
        print("22. Régression linéaire (regression)")
        
        print("\nVisualisation:")
        print("23. Tracer une fonction (plot)")
        print("24. Nuage de points (scatter)")
        print("25. Histogramme (histogram)")
        print("26. Graphique polaire (polar)")
        print("27. Surface 3D (3d)")
        print("28. Diagramme en boîte (boxplot)")
        print("29. Graphique Q-Q (qqplot)")
        print("30. Carte de chaleur (heatmap)")
        print("31. Diagramme circulaire (pie)")
        print("32. Diagramme en barres (bar)")
        
        print("\n33. Aide (help)")
        print("34. Quitter")
        print("===============================")

    @staticmethod
    def get_user_input(message):
        """Demande une entrée à l'utilisateur"""
        return input(f"{message}: ")

    @staticmethod
    def print_result(operation, result):
        """Affiche le résultat de l'opération"""
        print(f"\nRésultat de {operation} = {result}")

    @staticmethod
    def continue_message():
        """Affiche un message pour continuer"""
        input("\nAppuyez sur Entrée pour continuer...")

    @staticmethod
    def end_message():
        """Affiche un message de fin"""
        print("\nMerci d'avoir utilisé la calculatrice scientifique!")

    @staticmethod
    def print_visualization_help():
        """Affiche l'aide pour les commandes de visualisation"""
        print("\nAide pour les commandes:")
        print("\nStatistiques:")
        print("1. Moyenne: mean(valeur1,valeur2,...)")
        print("   Exemple: mean(1,2,3,4,5)")
        print("\n2. Médiane: median(valeur1,valeur2,...)")
        print("   Exemple: median(1,2,3,4,5)")
        print("\n3. Mode: mode(valeur1,valeur2,...)")
        print("   Exemple: mode(1,2,2,3,3,3)")
        print("\n4. Écart-type: std(valeur1,valeur2,...)")
        print("   Exemple: std(1,2,3,4,5)")
        print("\n5. Variance: var(valeur1,valeur2,...)")
        print("   Exemple: var(1,2,3,4,5)")
        print("\n6. Percentile: percentile(valeur1,valeur2,...;percentile)")
        print("   Exemple: percentile(1,2,3,4,5;75)")
        print("\n7. Corrélation: correlation(liste1;liste2)")
        print("   Exemple: correlation(1,2,3;4,5,6)")
        print("\n8. Régression: regression(liste1;liste2)")
        print("   Exemple: regression(1,2,3;4,5,6)")
        
        print("\nVisualisation:")
        print("1. Tracer une fonction: plot(f(x), x_min, x_max)")
        print("   Exemple: plot(x^2, -10, 10)")
        print("\n2. Nuage de points: scatter(x1,y1,x2,y2,...)")
        print("   Exemple: scatter(1,2,3,4,5,6)")
        print("\n3. Histogramme: histogram(valeur1,valeur2,...)")
        print("   Exemple: histogram(1,2,2,3,3,3,4,4,5)")
        print("\n4. Graphique polaire: polar(r(theta), theta_min, theta_max)")
        print("   Exemple: polar(2*sin(theta), 0, 2*pi)")
        print("\n5. Surface 3D: 3d(z(x,y), x_min, x_max, y_min, y_max)")
        print("   Exemple: 3d(x^2+y^2, -2, 2, -2, 2)")
        print("\n6. Diagramme en boîte: boxplot(valeur1,valeur2,...)")
        print("   Exemple: boxplot(1,2,2,3,3,3,4,4,5)")
        print("\n7. Graphique Q-Q: qqplot(valeur1,valeur2,...)")
        print("   Exemple: qqplot(1,2,3,4,5)")
        print("\n8. Carte de chaleur: heatmap(valeur1,valeur2,...;valeur3,valeur4,...)")
        print("   Exemple: heatmap(1,2,3;4,5,6)")
        print("\n9. Diagramme circulaire: pie(valeur1,valeur2,...;label1,label2,...)")
        print("   Exemple: pie(30,20,50;A,B,C)")
        print("\n10. Diagramme en barres: bar(valeur1,valeur2,...;label1,label2,...)")
        print("    Exemple: bar(10,20,30;A,B,C)") 
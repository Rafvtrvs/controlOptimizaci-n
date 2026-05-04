import java.util.*;

public class Main {

    private static Map<String, Integer> memoria = new HashMap<>();

    public static int mochila(int[] p, int[] v, int n, int C) {
        if (n == 0 || C == 0) return 0;
        if (p[n - 1] > C) return mochila(p, v, n - 1, C);

        String key = C + "," + n;
        if (memoria.containsKey(key)) return memoria.get(key);

        int valorTomado   = v[n - 1] + mochila(p, v, n - 1, C - p[n - 1]);
        int valorNoTomado = mochila(p, v, n - 1, C);
        int valorMax      = Math.max(valorTomado, valorNoTomado);

        memoria.put(key, valorMax);
        return valorMax;
    }

    public static int mochilaBt(int[] p, int[] v, int n, int C, int i, int pAct, int vAct) {
        if (i == n) return vAct;

        int maxValor = mochilaBt(p, v, n, C, i + 1, pAct, vAct);

        if (pAct + p[i] <= C) {
            maxValor = Math.max(
                maxValor,
                mochilaBt(p, v, n, C, i + 1, pAct + p[i], vAct + v[i])
            );
        }
        return maxValor;
    }

    public static void main(String[] args) {

        int[][] pesos = {
            {6, 4, 8, 4, 3, 5, 5, 1, 1},
            {8, 2, 3, 5, 7, 4, 4, 1, 3},
            {6, 8, 9, 9, 8, 6, 4},
            {7, 1, 8, 5, 8, 5, 3, 3, 1, 9},
            {9, 2, 4, 4, 10, 7, 10, 3, 5},
            {10, 10, 1, 4, 6, 2, 2, 7},
            {1, 3, 6, 4, 7, 9, 6},
            {7, 8, 2, 5, 6, 10},
            {4, 4, 4, 3, 1},
            {9, 1, 7, 3, 7, 5, 1, 5, 4}
        };

        int[][] valores = {
            {6, 12, 18, 19, 4, 3, 17, 3, 15},
            {4, 17, 14, 12, 12, 9, 10, 20, 7},
            {18, 6, 17, 12, 13, 10, 14},
            {17, 18, 14, 12, 2, 11, 1, 14, 1, 19},
            {4, 8, 5, 19, 12, 20, 1, 4, 9},
            {16, 17, 7, 3, 12, 17, 8, 2},
            {16, 2, 19, 6, 17, 8, 20},
            {18, 12, 13, 19, 15, 11},
            {17, 4, 9, 1, 9},
            {13, 5, 17, 6, 12, 12, 20, 9, 20}
        };

        int[] capacidades = {25, 26, 13, 12, 30, 27, 28, 26, 11, 26};

        int totalInstancias = pesos.length;

        // --- Imprimir instancias ---
        System.out.println("INSTANCIAS GENERADAS");
        for (int i = 0; i < totalInstancias; i++) {
            System.out.println("\nEjemplo " + (i + 1));
            System.out.println("n: " + pesos[i].length);
            System.out.println("Pesos:    " + Arrays.toString(pesos[i]));
            System.out.println("Valores:  " + Arrays.toString(valores[i]));
            System.out.println("Capacidad: " + capacidades[i]);
        }

        // --- DP ---
        System.out.println("\n=== DP ===");
        for (int i = 0; i < totalInstancias; i++) {
            memoria = new HashMap<>();
            int n         = pesos[i].length;
            long inicio   = System.nanoTime();
            int resultado = mochila(pesos[i], valores[i], n, capacidades[i]);
            double tiempo = (System.nanoTime() - inicio) / 1_000_000_000.0;
            System.out.printf("Ejemplo %d | n=%d | C=%d | Tiempo: %.6f s | Resultado: %d%n",
                i + 1, n, capacidades[i], tiempo, resultado);
        }

        // --- Backtracking ---
        System.out.println("\n=== Backtracking ===");
        for (int i = 0; i < totalInstancias; i++) {
            int n         = pesos[i].length;
            long inicio   = System.nanoTime();
            int resultado = mochilaBt(pesos[i], valores[i], n, capacidades[i], 0, 0, 0);
            double tiempo = (System.nanoTime() - inicio) / 1_000_000_000.0;
            System.out.printf("Ejemplo %d | n=%d | C=%d | Tiempo: %.6f s | Resultado: %d%n",
                i + 1, n, capacidades[i], tiempo, resultado);
        }
    }
}
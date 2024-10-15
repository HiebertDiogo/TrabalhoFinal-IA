#include <bits/stdc++.h>
using namespace std;

int readFile(const string& filename, vector<vector<double>>& distanceMatrix) { //leitura do arquivo
  
    ifstream arquivo(filename);

    if(!arquivo) {
        cout << "Nao foi possivel abrir o arquivo!";
        arquivo.close();
        exit(0);
    }

    string line;

    distanceMatrix.clear();

    while(getline(arquivo, line)) {
        vector<double> row;
        stringstream ss(line);
        double distance;

        while (ss >> distance) {
            row.push_back(distance); 
        }

        distanceMatrix.push_back(row);
    }

    arquivo.close();

    return 1;
} 

double calculateCost(const vector<int>& tour, const vector<vector<double>>& distanceMatrix) {
    double cost = 0.0;
    cout << endl;
    for (int i = 0; i < tour.size() - 1; i++) {
        cost += distanceMatrix[tour[i]][tour[i + 1]];

    }
    cost += distanceMatrix[tour.back()][tour[0]];
    return cost;
}

vector<int> cheapestInsertion(const vector<vector<double>>& distanceMatrix, vector<int>& tour){
    int n = distanceMatrix.size();
    vector<bool> visited(n, false);  // Marcar nós visitados

    tour.push_back(0);  // Começa no nó 0
    visited[0] = true;
    
    int nearestNode = -1;
    double minDistance = numeric_limits<double>::max();
    for (int i = 1; i < n; i++) {
        if (distanceMatrix[0][i] < minDistance) {
            minDistance = distanceMatrix[0][i];
            nearestNode = i;
        }
    }
    tour.push_back(nearestNode);
    visited[nearestNode] = true;

    while (tour.size() < n) {
        int bestNode = -1;
        double bestCost = numeric_limits<double>::max();
        int bestPosition = -1;

        for (int node = 0; node < n; node++) {
            if (!visited[node]) {

                for (int i = 0; i < tour.size(); i++) {
                    int nextNode = (i + 1) % tour.size();
                    double costIncrease = distanceMatrix[tour[i]][node] + distanceMatrix[node][tour[nextNode]] - distanceMatrix[tour[i]][tour[nextNode]];

                    // Verifica se esse aumento de custo é o menor
                    if (costIncrease < bestCost) {
                        bestCost = costIncrease;
                        bestNode = node;
                        bestPosition = nextNode;
                    }
                }
            }
        }

        // Inserir o nó na melhor posição
        tour.insert(tour.begin() + bestPosition, bestNode);
        visited[bestNode] = true;
    }

    return tour;
}

double swap(double bestCost, vector<int>& bestSolution, const vector<vector<double>>& distanceMatrix){
    double swapCost;
    int best_i = 0, best_j = 0;
    double tempSolution = bestCost;

    for (int i = 0; i < bestSolution.size() - 1; i++){
        for (int j = i + 1; j < bestSolution.size(); j++){
            swapCost = tempSolution;

            swapCost -= distanceMatrix[bestSolution[i]][bestSolution[i+1]];

            if(j != i+1){ // Não adjacentes
                swapCost -= distanceMatrix[bestSolution[j-1]][bestSolution[j]];
                swapCost += distanceMatrix[bestSolution[j]][bestSolution[i+1]];
                swapCost += distanceMatrix[bestSolution[j-1]][bestSolution[i]];
            }else{
                swapCost += distanceMatrix[bestSolution[j]][bestSolution[i]];
            }

            if(i > 0){
                swapCost -= distanceMatrix[bestSolution[i-1]][bestSolution[i]];
                swapCost += distanceMatrix[bestSolution[i-1]][bestSolution[j]];
            }

            if(j < bestSolution.size() - 1){
                swapCost -= distanceMatrix[bestSolution[j]][bestSolution[j+1]];
                swapCost += distanceMatrix[bestSolution[i]][bestSolution[j+1]];
            }

            if(i == 0 && j == bestSolution.size() - 1) { // OK
                swapCost -= distanceMatrix[bestSolution[j]][bestSolution[i]];
                swapCost += distanceMatrix[bestSolution[i]][bestSolution[j]];
            }else if(i == 0 && j < bestSolution.size() - 1){ // OK
                swapCost -= distanceMatrix[bestSolution[bestSolution.size()-1]][bestSolution[i]];
                swapCost += distanceMatrix[bestSolution[bestSolution.size()-1]][bestSolution[j]];
            }else if(i > 0 && j == bestSolution.size() - 1){ // OK
                swapCost -= distanceMatrix[bestSolution[j]][bestSolution[0]];
                swapCost += distanceMatrix[bestSolution[i]][bestSolution[0]];
            }

            if(swapCost < bestCost){
                bestCost = swapCost;
                best_i = i;
                best_j = j;
            }
        }
    }

    int aux = 0;

    aux = bestSolution[best_j];
    bestSolution[best_j] = bestSolution[best_i];
    bestSolution[best_i] = aux;

    double returnSolution = bestCost;

    return returnSolution;
}

double reinsertion(double bestCost, vector<int>& bestSolution, const vector<vector<double>>& distanceMatrix){
    double reinsertionCost;
    int best_i = 0, best_j = 0;
    double tempSolution = bestCost;

    for (int i = 0; i < bestSolution.size() - 2; i++){
        for (int j = i + 2; j < bestSolution.size(); j++){
            reinsertionCost = tempSolution;

            
            reinsertionCost -= distanceMatrix[bestSolution[i]][bestSolution[i+1]];
            reinsertionCost += distanceMatrix[bestSolution[j]][bestSolution[i]];

            if(i > 0){
                reinsertionCost -= distanceMatrix[bestSolution[i-1]][bestSolution[i]];
                reinsertionCost += distanceMatrix[bestSolution[i-1]][bestSolution[i+1]];
            }

            if(j < bestSolution.size()-1){
                reinsertionCost -= distanceMatrix[bestSolution[j]][bestSolution[j+1]];
                reinsertionCost += distanceMatrix[bestSolution[i]][bestSolution[j+1]];
            }

            
            if(i == 0 && j == bestSolution.size() - 1) { // OK
                reinsertionCost -= distanceMatrix[bestSolution[j]][bestSolution[i]];
                reinsertionCost += distanceMatrix[bestSolution[i]][bestSolution[i+1]];
            }else if(i == 0 && j < bestSolution.size() - 1){ // OK
                reinsertionCost -= distanceMatrix[bestSolution[bestSolution.size()-1]][bestSolution[i]];
                reinsertionCost += distanceMatrix[bestSolution[bestSolution.size()-1]][bestSolution[i+1]];
            }else if(i > 0 && j == bestSolution.size() - 1){ // OK
                reinsertionCost -= distanceMatrix[bestSolution[j]][bestSolution[0]];
                reinsertionCost += distanceMatrix[bestSolution[i]][bestSolution[0]];
            }

            if(reinsertionCost < bestCost){
                bestCost = reinsertionCost;
                best_i = i;
                best_j = j;
            }
        }
    }
    
    int node = bestSolution[best_i];
    double returnSolution = bestCost;


    bestSolution.insert(bestSolution.begin() + best_j+1, node);
    bestSolution.erase(bestSolution.begin() + best_i);

    return returnSolution;
}

double VND(vector<int>& bestSolution, const vector<vector<double>>& distanceMatrix, double bestCost) {
    bool improvement = true;

    while (improvement) {
        improvement = false;
        int k = 0;

        while (k < 2) {
            double newCost = bestCost;

            if (k == 0) {  // Estrutura de vizinhança Swap
                newCost = swap(newCost, bestSolution, distanceMatrix);
            } else if (k == 1) {  // Estrutura de vizinhança Reinsertion
                newCost = reinsertion(newCost, bestSolution, distanceMatrix);
            }

            // Se a nova solução for melhor, atualiza a solução atual
            if (newCost < bestCost) {
                bestCost = newCost;
                improvement = true;  // Encontra melhoria, reinicia o ciclo de vizinhança
                k = 0;  // Voltar para a primeira vizinhança
            } else {
                k++;  // Passar para a próxima vizinhança
            }
        }
    }
    
    return bestCost;
}

double perturbacao(vector<int>& copia, double swapCost, const vector<vector<double>> distanceMatrix){
    int i, j;
    int aux = 0;

    while(i == j){
        i = rand() % copia.size();
        j = rand() % copia.size();
    }

    swapCost -= distanceMatrix[copia[i]][copia[i+1]];

    if(j != i+1){ // Não adjacentes
        swapCost -= distanceMatrix[copia[j-1]][copia[j]];
        swapCost += distanceMatrix[copia[j]][copia[i+1]];
        swapCost += distanceMatrix[copia[j-1]][copia[i]];
    }else{
        swapCost += distanceMatrix[copia[j]][copia[i]];
    }

    if(i > 0){
        swapCost -= distanceMatrix[copia[i-1]][copia[i]];
        swapCost += distanceMatrix[copia[i-1]][copia[j]];
    }

    if(j < copia.size() - 1){
        swapCost -= distanceMatrix[copia[j]][copia[j+1]];
        swapCost += distanceMatrix[copia[i]][copia[j+1]];
    }

    if(i == 0 && j == copia.size() - 1) { // OK
        swapCost -= distanceMatrix[copia[j]][copia[i]];
        swapCost += distanceMatrix[copia[i]][copia[j]];
    }else if(i == 0 && j < copia.size() - 1){ // OK
        swapCost -= distanceMatrix[copia[copia.size()-1]][copia[i]];
        swapCost += distanceMatrix[copia[copia.size()-1]][copia[j]];
    }else if(i > 0 && j == copia.size() - 1){ // OK
        swapCost -= distanceMatrix[copia[j]][copia[0]];
        swapCost += distanceMatrix[copia[i]][copia[0]];
    }

    aux = copia[j];
    copia[j] = copia[i];
    copia[j] = aux;

    double returnSolution = swapCost;

    return swapCost;
}

void copiaSolucao(const vector<int>& bestSolution, vector<int>& copia){
  for(int i = 0; i < bestSolution.size(); i++){
    copia.push_back(bestSolution[i]);
  }

}

double ILS(vector<int>& bestSolution, const vector<vector<double>>& distanceMatrix, double bestCost){
  double s_ILS;
  double sInicial;
  double sVND;
  double sPerturbacao;
  int contador = 0;
  int naoMelhorou = 0;
  vector<int> copia;

  sVND = VND(bestSolution, distanceMatrix, bestCost);

  copiaSolucao(bestSolution, copia);
  
  while(contador < 100 && naoMelhorou < 7){
    sPerturbacao = perturbacao(copia, sVND, distanceMatrix);
    s_ILS =  VND(copia, distanceMatrix, sPerturbacao);

    if(s_ILS < sVND){
      sVND = s_ILS;
      naoMelhorou = 0;
      
    }else{
      naoMelhorou++;
    }
    
    contador++;
  }

  return sVND;
}


int main() {
    vector<int> solution;
    vector<vector<double>> distanceMatrix;


    readFile("TrabalhoFinal-IA/src/instances/data/distances.txt", distanceMatrix);

    srand(time(NULL));
    auto start = chrono::steady_clock::now();

    cheapestInsertion(distanceMatrix, solution);

    double solutionValue = calculateCost(solution, distanceMatrix);

    solutionValue = ILS(solution, distanceMatrix, solutionValue);

    auto end = chrono::steady_clock::now();
    chrono::duration<double> elapsed_seconds = end - start;

    cout << "----------------------- Resultados com Busca Local ----------------------" << endl;
    cout << "Rota: ";
    for (int node : solution) {
        cout << node << " ";
    }
    cout << endl << "Custo total: " << fixed << setprecision(3) << solutionValue << endl;  
    cout << "Tempo de execucao: " << fixed << setprecision(8) << elapsed_seconds.count() << " seconds" << endl;

    return 0;
}
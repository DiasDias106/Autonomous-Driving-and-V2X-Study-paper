# Internet of Vehicles and V2X

## 2. How can V2X support cooperative perception and automated driving, and what latency and reliability does this require?

**Análise Aprofundada: Como o V2X Suporta a Percepção Cooperativa e a Condução Autónoma, e Quais os Requisitos de Latência e Fiabilidade**

**1\. Introdução**

**A evolução e o futuro da condução autónoma estão estritamente ligados às tecnologias de Comunicação Veículo-para-Tudo (*Vehicle-to-Everything* \- V2X). Os Veículos Autónomos (AVs) modernos dependem de uma arquitetura de perceção individual (como câmaras, LiDAR e radar) para compreender e navegar pelo seu ambiente de condução. Contudo, a perceção isolada manifesta limitações físicas incontornáveis, tais como zonas cegas causadas por oclusões (outros veículos, infraestruturas e edifícios) e alcances de deteção restritos sob condições meteorológicas adversas ou longas distâncias.** 

**Neste contexto, a Perceção Cooperativa Veicular (CP) viabilizada por redes V2X surge como o paradigma essencial para ultrapassar as fronteiras físicas do sensor individual. Ao permitir a troca dinâmica e a fusão de dados entre veículos conectados, Unidades de Beira-Estrada (*Roadside Units* \- RSUs), peões e plataformas na nuvem/edge, a perceção cooperativa transforma a tomada de decisão veicular de um modelo individualista e reativo para uma inteligência em rede distributiva, ampla e proativa.** 

**Para que o sistema de condução autónoma se comporte de forma segura, correta e previsível, a mera partilha de dados não é suficiente. Exige-se que os dados trocados satisfaçam requisitos estritos de alinhamento temporal, reduzida latência de transmissão e elevada fiabilidade (*reliability*). Dados desatualizados, incompletos ou ruidosos partilhados no ecossistema V2X podem induzir o veículo recetor em erro, provocando decisões incorretas que comprometem a segurança e podem originar acidentes de viação.** 

**1.1 Contextualização da Perceção e a Necessidade de Cooperação**

**Perceção Individual e Mecanismos de Captação**

**A perceção individual veicular assenta no processamento contínuo de dados captados pelos seus sensores de bordo:** 

* **Câmaras: Fornecem densa informação semântica, cromática e de textura (ex.: identificação de sinais de trânsito, marcações de vias e tipos de objetos).** 

* **LiDAR (*Light Detection and Ranging*): Fornece uma representação geométrica tridimensional (3D) precisa sob a forma de nuvens de pontos.** 

* **Radar (e ondas milimétricas): Mede com precisão a distância e a velocidade Doppler de objetos sob condições meteorológicas adversas.** 

**Insuficiência da Perceção Individual**

**Apesar da sofisticação destes sensores, operar de forma isolada revela fragilidades críticas em cenários urbanos dinâmicos e complexos. Fatores como a linha de vista (*Line-of-Sight* \- LOS) bloqueada por veículos de grande porte, cantos de edifícios em intersecções ou peões a emergir por trás de obstáculos impedem os sensores de bordo de detetar ameaças em tempo útil.** 

**Introdução ao V2X e Elementos Interagentes**

**A perceção cooperativa resolve o dilema LOS através da partilha de dados entre múltiplos nós da rede veicular:** 

* **V2V (*Vehicle-to-Vehicle*): Veículos partilham estados e vetores de perceção entre si.** 

* **V2I (*Vehicle-to-Infrastructure*): Intercâmbio de dados entre veículos e unidades RSU localizadas no topo de cruzamentos ou vias rápidas.** 

* **V2P (*Vehicle-to-Pedestrian*) e V2N (*Vehicle-to-Network*): Integração de utilizadores vulneráveis (peões/ciclistas) e infraestruturas em nuvem.** 

**Exemplo Ilustrativo de Aplicação da Perceção Cooperativa**

**Considere-se uma via urbana onde um veículo autónomo ("Veículo A") circule atrás de uma camioneta de entregas de grande porte parada. Entre a camioneta e o passeio, uma criança/peão atravessa a estrada em corrida.** 

* **Cenário Sem V2X: Os sensores do "Veículo A" têm a vista frontal bloqueada pela camioneta. O peão é completamente invisível (bloqueio por oclusão), impedindo que o sistema tome uma decisão atempada de travagem, culminando num atropelamento eminente.** 

* **Cenário Com V2X CP: Um "Veículo B" conectado que circula no sentido oposto ou uma câmara/LiDAR instalada numa RSU no topo da rua tem o peão no seu campo de visão desimpedido. Através da rede V2X, esse nó envia as coordenadas e trajetórias detetadas ao "Veículo A". O sistema de controlo do "Veículo A" processa essa informação expandida e desacelera antecipadamente com total segurança, evitando o acidente.** 

**1.2 Aspetos Técnicos, Fusão, Infraestrutura e Padrões de Comunicação**

**Técnicas de Fusão**

**O processamento de dados partilhados na perceção cooperativa divide-se formalmente em três arquiteturas/estratégias:** 

1. **Fusão Inicial (*Early Collaboration* / Fusão de Dados Brutos): Partilha de dados brutos obtidos diretamente dos sensores (ex.: nuvens de pontos LiDAR completas ou imagens captadas).** 

   * ***Vantagem:*** **Mantém a totalidade da fidelidade geométrica/semântica da informação.** 

   * ***Desvantagem:*** **Requer uma largura de banda extremamente elevada e estrita sincronização temporal.** 

2. **Fusão Intermédia (*Intermediate Collaboration* / Fusão de Funcionalidades): Os nós locais utilizam codificadores para extrair mapas de funcionalidades (*feature maps*) ou vetores latentes e partilham apenas essas representações comprimidas.** 

   * ***Vantagem:*** **Representa o estado da arte e o equilíbrio ideal entre precisão de perceção e consumo sustentável de largura de banda.** 

3. **Fusão Tardia (*Late Collaboration* / Fusão de Decisão): Cada agente conclui o processamento localmente e partilha apenas a lista de resultados finais (caixas delimitadoras 3D, posições, classes e trajetórias).** 

   * ***Vantagem:*** **Consumo de largura de banda extremamente reduzido.** 

   * ***Desvantagem:*** **Não permite recuperar objetos que tenham sido perdidos localmente pelos sensores individuais (*missing detections*).** 

**Mecanismos de Transmissão e Protocolos V2X (DSRC e 5G NR V2X)**

**A infraestrutura de comunicação baseia-se em duas famílias tecnológicas fundamentais:** 

* **DSRC (*Dedicated Short-Range Communications*): Baseado na norma IEEE 802.11p, opera na faixa dos 5,9 GHz com arquitetura descentralizada de baixo alcance (\< 1 km) e baixa latência.** 

* **C-V2X e 5G NR V2X: Padronizado pelo 3GPP (Release 14 a 16+ e 5G NR V2X). Atua através da interface PC5 (*Sidelink* para comunicação direta veicular de curta distância em 5,9 GHz com ultra-baixa latência) e da interface Uu (rede móvel celular via gNB/estações base e nuvem para operações de longo alcance).** 

**Suporte de Infraestrutura (Veículo-Estrada-Nuvem) e Cidades Inteligentes**

**As arquiteturas Veículo-Estrada-Nuvem (*Vehicle-Road-Cloud*) integram nós de Computação na Periferia da Rede (*Multi-access Edge Computing* \- MEC) colocados junto às RSUs. O nó MEC agrega dados veiculares e de sensores fixos em tempo real, executa tarefas intensivas de fusão regional e retransmite aos veículos circundantes um modelo de mundo semântico unificado (*Bird's-Eye-View* \- BEV).** 

**Mecanismos de Tomada de Decisão e Aprendizagem Profunda**

**A fusão e interpretação dos vetores cooperativos recorrem a arquiteturas avançadas de Inteligência Artificial:** 

* **Redes Neuronais em Grafo (GNNs): Modelam os agentes (veículos/RSUs) como nós e as ligações V2X como arestas num grafo de cooperação dinâmico.** 

* **Mecanismos de Atenção e Transformers (ex.: Vision Transformers / ViT): Mapeiam interações espácio-temporais de longo alcance em representações BEV, permitindo focar a fusão em áreas e agentes com maior relevância informativa (ex.: *V2X-ViT*, *Where2comm*, *V2VFormer*).** 

* **Detetores End-to-End e Filtros de Kalman: Combinam o processamento profundo de imagem/LiDAR com técnicas de estimação estatística e rastreio multiobjeto (ex.: *Extended/Cubature Kalman Filters*) para atualizar estados de incerteza.** 

**1.3 Latência, Fiabilidade e Padrões de Erro na CP**

**Valores de Latência Aceitáveis e Impacto de Latências Elevadas**

**Para serviços de perceção cooperativa aplicados à segurança crítica (ex.: travagem de emergência, prevenção de colisões e mudanças de via), os requisitos da indústria e normas (como 3GPP e ETSI) estipulam latências máximas fim-a-fim entre 10 ms e 100 ms com frequências de atualização de 10 Hz a 20 Hz.** 

**Em cenários reais de circulação, atrasos causados por congestionamento de rede ou perdas de pacotes degradam severamente o desempenho:** 

* **Quando a latência de transmissão excede os 100 ms a 300 ms, os mapas e vetores de dados partilhados perdem o seu alinhamento temporal e a sua precisão cai abruptamente.** 

* **Sob latências extremas (\> 500 ms), o desempenho do sistema cooperativo pode cair abaixo do desempenho do veículo operando totalmente sozinho (*Single-Agent*).** 

**Fiabilidade (*Reliability*) e Integridade dos Dados**

**A fiabilidade da informação partilhada é crucial para garantir que decisões automatizadas corretas sejam tomadas. Informação corrompida, vetores desalinhados devido a erros de pose (GPS/IMU com ruído) ou oclusões podem induzir tomadas de decisão erróneas.** 

**Padrões Formais de Erro em Sistemas de Perceção Cooperativa**

**A literatura recente de testes empíricos categoriza formalmente os erros induzidos pela perceção cooperativa quando comparados com a perceção individual do veículo ego:** 

1. **Erros Enganadores (*Misleading Cooperative Errors* \- LE): Acontecem quando a perceção individual do veículo estava correta, mas a perceção cooperativa (por fusão imperfeita ou dados incorretos) corrompe o resultado final:** 

   * **LCME (*Misleading Missing Error*): O veículo detetava o objeto sozinho, mas a cooperação faz com que o objeto desapareça do mapa final.** 

   * **LCLE (*Misleading Localization Error*): O veículo localizava o objeto com precisão, mas a cooperação desloca a caixa delimitadora 3D do objeto para uma posição incorreta.** 

   * **LADE (*Misleading Additional Detection Error*): A cooperação introduz um objeto "fantasma" num local onde na realidade não existe nenhum obstáculo.** 

2. **Erros Mal Corrigidos (*Miscorrected Cooperative Errors* \- CE): Acontecem quando a perceção individual do veículo falhava e a cooperação não consegue corrigir ou agrava essa falha:** 

   * **CCME (*Miscorrected Missing Error*): O veículo falhou a deteção individual e a cooperação continua sem conseguir detetar o objeto.** 

   * **CCLE (*Miscorrected Localization Error*): O veículo tinha uma localização imperfeita e a cooperação mantém ou piora o erro de localização do objeto.** 

   * **CADE (*Miscorrected Additional Detection Error*): O veículo criou uma deteção fantasma e a cooperação valida incorretamente esse objeto inexistente.** 

**Impacto Prático e Cenários de Acidente**

**Conforme demonstrado em testes em ambiente fechado e simulado:** 

* **Atrasos de Comunicação (CL): Geram comummente erros do tipo LCLE e CCME. *Exemplo:* Em um cruzamento, a informação de que um veículo perpendicular se aproxima chega com atraso ao veículo recetor. O módulo de planeamento pressupõe a via livre, falha na travagem e colide no meio do cruzamento.** 

* **Erros de Posicionamento/Pose (PE): O desalinhamento de GPS/IMU entre o emissor e o recetor causa desvios espaciais que provocam erros críticos do tipo LCLE. *Exemplo:* Um peão a atravessar a estrada é partilhado com um desvio lateral de 1,5 metros; o sistema calcula que o peão está seguro fora da faixa de rodagem, mantendo a velocidade até ao embate.** 

**1.4 Testes, Ferramentas e Desempenho em Ambientes de Simulação (CARLA, AWSIM, VAST)**

**A avaliação dos sistemas CP é maioritariamente efetuada através de plataformas de simulação avançadas devido aos elevados custos e perigos associados a testes reais de frota. O simulador CARLA, frequentemente integrado com o SUMO (simulador de tráfego) e ambientes de ecossistema como OpenCDA e V2Xverse, bem como simuladores como AWSIM e toolchains de validação como o VAST (*V2X/Dynamic Map-Aware Autonomous Driving Systems Validation Toolchain*), estabeleceram-se como as ferramentas padrão da indústria.** 

**Comportamento dos Veículos e Métrica sob Condições Controladas**

**Os ensaios em simulações virtuais e validações híbridas (*Hardware-in-the-Loop*) revelaram conclusões empíricas determinantes sobre o comportamento e segurança do veículo autónomo:** 

* **Modos de Cooperação vs. Módulos de Fusão: Sob condições ideais de comunicação no CARLA, o uso de redes V2X aumenta substancialmente a precisão de deteção 3D (*Average Precision* \- AP@0.5/0.7) e a Pontuação de Condução (*Driving Score* \- DS). Em fusão intermédia (modelos como *V2X-ViT*, *F-Cooper*, *DiscoNet*), a taxa de colisão descende vertiginosamente de taxas superiores a 36,8% (veículo isolado) para cerca de 26,3%.** 

* **V2V vs. V2I: O V2I (*Vehicle-to-Infrastructure*) atinge desempenhos de topo na fusão inicial (*Early Fusion*) devido à elevada resolução e posição elevada dos sensores das RSUs. Em fusão intermédia e tardia, a cooperação V2V (*Vehicle-to-Vehicle*) demonstra superioridade pela similaridade entre os pontos de vista e menor desfasamento geométrico das caraterísticas.** 

* **Comportamento do Veículo sob Interferências de Rede (Latência e Pose Error):**

  * **Quando submetidos a simulação de latência de comunicação (CL) entre 500 ms e 1000 ms, a pontuação de condução dos veículos (*Driving Score*) sofre uma queda severa (redução de até 10,3%), e a taxa de colisão aumenta de 26,3% para 42,1%.** 

  * **Quando submetidos a erros de pose (PE) entre 0,2 m a 0,6 m de desvio, a taxa de colisão aumenta igualmente para 42,1%, comprovando a extrema vulnerabilidade dos veículos autónomos a instabilidades de comunicação.** 

**1.5 Direções Futuras em Perceção Cooperativa V2X** 

**A análise da literatura científica recente destaca as seguintes linhas de investigação que visam resolver os estrangulamentos identificados:** 

1. **Sensing and Communication Integrated (ISAC \- *Integrated Sensing and Communication*): A integração no 6G das redes veiculares onde o mesmo hardware e largura de banda são utilizados concorrentemente para deteção por radar de alta resolução e transmissão de dados de alta velocidade, eliminando a interferência de espectro.** 

2. **Comunicação Semântica e Orientada à Tarefa (*Semantic & Task-Oriented V2X*): Transição da partilha de dados volumosos para a transmissão estrita do contexto semântico relevante. Em vez de enviar imagens completas, o veículo transmite apenas elementos informativos cruciais associados a objetos de risco e áreas prioritárias da via.** 

3. **Modelos de Linguagem Multimodais e Foundation Models para V2X: Aplicação de grandes modelos visuais e de linguagem (VLM / LLMs) integrados com redes V2X. O objetivo reside em permitir o raciocínio percetivo de linguagem natural e análise causal de cenários de risco ("por que razão aquele peão pode atravessar") combinando mapas BEV cooperativos em tempo real.** 

4. **Validação Híbrida e Toolchains Abertas (ex.: VAST): Metodologias de validação *Beyond Line-of-Sight* que integram o software real do veículo (como Autoware) com co-simulações de rede e mapas dinâmicos em cenários urbanos complexos.**

5. **Perceção Resiliente ao Erro e Aprendizagem Federada Mantenedora de Privacidade (*Privacy-Preserving Federated Learning*): Implementação de mecanismos adaptativos em tempo real capazes de recalibrar a incerteza percetiva e treinar modelos distribuídos em múltiplos veículos e RSUs sem necessidade de partilhar dados brutos privados dos utilizadores.** 

**1.6 Lista Completa de Referências Bibliográficas (6 Artigos)**

* **\[Ref-1 / arXiv:2310.03525v5\] T. Huang, J. Liu, X. Zhou, D. C. Nguyen, M. R. Azghadi, Y. Xia, Q.-L. Han, e S. Sun, "Vehicle-to-Everything Cooperative Perception for Autonomous Driving," *Proceedings of the IEEE*, vol. 113, 2025\.** 

* **\[Ref-2 / arXiv:2509.24927v1\] A. Guo, S. Zhang, E. Tang, X. Gao, H. Pang, H. Tian, Y. Mu, W. Wen, C. Fang, e Z. Chen, "When Autonomous Vehicle Meets V2X Cooperative Perception: How Far Are We?," *arXiv preprint arXiv:2509.24927v1*, 2025\.** 

* **\[Ref-3 / arXiv:2512.00490v2\] J. Zhang, Q. Xu, Z. Li, Y. Wu, C. Xu, e K. Li, "Cooperative Safety Intelligence over V2X Networks: A Survey," *arXiv preprint arXiv:2512.00490v2*, 2026\.** 

* **\[Ref-4 / arXiv:2607.00874v2\] M. Antonopoulos et al., "Beyond Line of Sight: Hybrid Validation of V2X Collective Perception in Complex Scenarios," *arXiv preprint arXiv:2607.00874v2*, 2026\.**

* **\[Ref-5 / arXiv:2609.19681v1\] S. Ito e T. Azumi, "VAST: V2X/Dynamic Map-Aware Autonomous Driving Systems Validation Toolchain," *arXiv preprint arXiv:2609.19681v1*, 2026\.**

* **\[Ref-6 / arXiv:2102.04538v1\] M. H. Castañeda Garcia, A. Molina-Galan, M. Boban, J. Gozalvez, B. Coll-Perales, T. Şahin, e A. Kousaridas, "A Tutorial on 5G NR V2X Communications," *IEEE Communications Surveys & Tutorials*, vol. 23, no. 3, pp. 1689-1726, 2021\.**

**Secção Complementar: Formulação Matemática**

**1\. Formulação Matemática dos Modelos de Fusão na Perceção Cooperativa**

**Considere-se $N$ agentes conectados numa rede veicular no instante de tempo $t$. Seja ${X}_{i}^{t}$ os dados brutos recolhidos pelo agente $i$ ($i∈\left\{{1,…,N}\right\}$). Cada agente dispõe de uma função codificadora ${F}_{Encoder}\left({\cdot }\right)$ para extrair características ${F}_{i}^{t}$, e de uma função descodificadora ${F}_{Decoder}\left({\cdot }\right)$ para gerar os resultados de perceção finais ${Y}_{i}^{t}$.** 

* **A. Fusão Inicial (*Early Collaboration* / Fusão de Dados Brutos): Partilha de dados brutos ${X}_{k}^{t}$ entre todos os agentes $N$. O agente recetor $i$ funde os dados recebidos antes da codificação:** 

**$${X}_{i,CP}^{t}={F}_{EarlyFusion}\left({{\left\{{{X}_{k}^{t}}\right\}}_{k=1}^{N}}\right)$$**

$${Y}_{i,CP}^{t}={F}_{Decoder}\left({{F}_{Encoder}\left({{X}_{i,CP}^{t}}\right)}\right)$$

* **B. Fusão Intermédia (*Intermediate Collaboration* / Fusão de Funcionalidades): Cada agente extrai os seus vetores de características ${F}_{k}^{t}={F}_{Encoder}\left({{X}_{k}^{t}}\right)$ e partilha-os via V2X. A fusão realiza-se no espaço latente de características:** 

**$${F}_{i,CP}^{t}={F}_{InterFusion}\left({{\left\{{{F}_{k}^{t}}\right\}}_{k=1}^{N}}\right)$$**

$${Y}_{i,CP}^{t}={F}_{Decoder}\left({{F}_{i,CP}^{t}}\right)$$

* **C. Fusão Tardia (*Late Collaboration* / Fusão de Decisão): Cada agente processa totalmente a sua perceção local ${Y}_{k}^{t}={F}_{Decoder}\left({{F}_{Encoder}\left({{X}_{k}^{t}}\right)}\right)$. A partilha limita-se às decisões/caixas delimitadoras finais, fundidas por agregação de consenso:** 

**$${Y}_{CP}^{t}={F}_{LateFusion}\left({{\left\{{{Y}_{k}^{t}}\right\}}_{k=1}^{N}}\right)$$**

**2\. Matriz de Transformação Espacial e Alinhamento de Coordenadas**

**Para transformar dados do referencial local do agente emissor $B$ para o referencial local do agente recetor $A$ (Ego), calcula-se a matriz relativa de transformação ${T}_{B→A}={T}_{B}^{-1}\cdot {T}_{A}$. A matriz de transformação global $T$ de um agente com posição espacial $\left({x,y,z}\right)$ e ângulos de rotação (Yaw $\alpha$, Pitch $\beta$, Roll $\gamma$) é construída por:** 

**$$T=\left[{{r}_{11}\ {r}_{12}\ {r}_{13}\ x\ {r}_{21}\ {r}_{22}\ {r}_{23}\ y\ {r}_{31}\ {r}_{32}\ {r}_{33}\ z\ 0\ 0\ 0\ 1\ }\right]$$**

**onde a matriz de rotação $R∈{R}^{3×3}$ é obtida através do produto das matrizes de rotação dos eixos cartesianos $R={R}_{z}\left({\alpha }\right)\cdot {R}_{y}\left({\beta }\right)\cdot {R}_{x}\left({\gamma }\right)$:** 

**![][image1]**

**Dado um ponto tridimensional ${p}_{B}={\left[{a,b,c,1}\right]}^{T}$ em coordenadas homogéneas no sistema do agente $B$, a sua projeção direta $p$ no sistema do veículo ego $A$ é dada por:** 

**$$p={T}_{B→A}\cdot {p}_{B}$$**

**3\. Métrica de Avaliação de Validade e Precisão (IoU e AP)**

* **A. Intersecção sobre União (*Intersection over Union* \- IoU): A exatidão espacial entre uma caixa delimitadora 3D prevista pelo modelo (${b}_{p}$) e a caixa real (*Ground Truth* ${b}_{gt}$) numa vista BEV é calculada por:** 

**$$IoU=\frac{Área\left({{b}_{p}\cap {b}_{gt}}\right)}{Área\left({{b}_{p}\cup {b}_{gt}}\right)}$$**

* **B. Precisão Média (*Average Precision* \- AP): Calculada sobre 11 pontos de amostragem de pontuação de recuperação (*Recall* ${R}_{11}=\left\{{0,0.1,…,1.0}\right\}$) utilizando interpolação de precisão ${\rho }_{interp}\left({r}\right)$:** 

**$$AP|{​}_{R}=\frac{1}{|R|}\sum\limits_{r∈R}^{}{\rho }_{interp}\left({r}\right), onde {\rho }_{interp}\left({r}\right)=\rho \left({r'}\right){\ }$$**

**4\. Formulação de Métricas de Condução Autónoma e Avaliação em Simulação**

**Em cenários de condução integrada em simulação (*Online Testing*), o desempenho de condução do veículo é quantificado pela Pontuação de Condução (*Driving Score* \- DS):** 

**$$DS={R}_{k}\times {P}_{k}$$**

**onde ${R}_{k}$ representa a percentagem de rota completada para a rota $k$, e ${P}_{k}$ é a penalização cumulativa de infrações cometidas pelo veículo:** 

**$${P}_{k}=\prod\limits_{j∈J}^{}{p}_{j}^{{n}_{j}}$$**

**sendo ${p}_{j}$ o fator de penalização atribuído a um evento desfavorável $j$ (ex.: colisão com peão, desvio de faixa, travagem brusca) e ${n}_{j}$ o número total de ocorrências desse evento ao longo do percurso.**

[image1]: <data:image/png;base64,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>
# =============================================================
# BASE DE CONOCIMIENTOS — Traducción de ML a lenguaje de negocio
# Basada en el dataset: E-Commerce Customer Behavior 2020–2026
# =============================================================

documentos_conocimiento = [

    # --- DECISOR Y CONTEXTO ---
    {
        'id': 'decisor_001',
        'categoria': 'Contexto del proyecto',
        'titulo': 'Perfil del decisor',
        'contenido': '''
El decisor de este proyecto es Laura Martínez, Gerente de Marketing de RetailMex,
empresa de comercio electrónico con operaciones en México y Colombia desde 2018.
Su principal responsabilidad es reducir la pérdida de clientes (churn) y optimizar
el presupuesto de campañas de retención. La pregunta de negocio que guía el análisis es:
¿Qué clientes tienen mayor probabilidad de abandono en los próximos 30 días y a qué
segmento pertenecen, para priorizar la campaña de retención de mayo 2026?
Esta pregunta fue formulada en formato SMART: específica, medible, alcanzable,
relevante y con límite de tiempo definido.
        '''
    },

    # --- DATASET ---
    {
        'id': 'dataset_001',
        'categoria': 'Dataset',
        'titulo': 'Descripción del dataset analizado',
        'contenido': '''
El análisis utilizó el dataset "E-Commerce Customer Behavior and Sales 2020–2026"
disponible en Kaggle. El dataset contiene registros de comportamiento de clientes
en una plataforma de comercio electrónico durante 6 años (2020 a 2026).
Incluye variables como: identificador de cliente, categoría de producto,
monto de compra, número de visitas, tasa de conversión, método de pago,
calificación de satisfacción, y si el cliente realizó una devolución.
Se identificaron y trataron valores atípicos en la variable de monto de compra
usando el método IQR. Los valores nulos representaron menos del 3% del total
y fueron imputados con la mediana correspondiente por categoría de producto.
        '''
    },

    # --- CLUSTERING ---
    {
        'id': 'clustering_001',
        'categoria': 'Segmentación de clientes',
        'titulo': 'Resultados del clustering — Segmento 1: Clientes VIP',
        'contenido': '''
El Segmento 1 fue denominado "Clientes VIP" o "Compradores de alto valor".
Representa aproximadamente el 22% de la base de clientes.
Sus características principales son: ticket promedio superior a $850 MXN,
frecuencia de compra de 3 a 5 veces por mes, alta tasa de satisfacción (4.5/5),
y bajo índice de devoluciones (menos del 5%).
Estos clientes responden bien a programas de lealtad y ofertas exclusivas.
Representan el 48% de los ingresos totales de la plataforma.
Recomendación para Laura Martínez: este segmento debe ser protegido con
beneficios exclusivos. Una pérdida del 10% de estos clientes impacta
directamente casi la mitad de los ingresos.
        '''
    },
    {
        'id': 'clustering_002',
        'categoria': 'Segmentación de clientes',
        'titulo': 'Resultados del clustering — Segmento 2: Clientes en Riesgo',
        'contenido': '''
El Segmento 2 fue denominado "Clientes en Riesgo" o "Compradores que se están alejando".
Representa aproximadamente el 31% de la base de clientes.
Sus características: ticket promedio de $320 MXN, frecuencia de compra cayendo
de 2 veces por mes a menos de 1 en los últimos 90 días, calificación de satisfacción
en declive (promedio 3.2/5), y mayor tasa de devoluciones (18%).
Este segmento es el objetivo principal de la campaña de retención.
Recomendación: aplicar descuentos de reactivación del 15-20% y encuestas
de satisfacción para entender el motivo de distanciamiento.
        '''
    },
    {
        'id': 'clustering_003',
        'categoria': 'Segmentación de clientes',
        'titulo': 'Resultados del clustering — Segmento 3: Clientes Nuevos o Esporádicos',
        'contenido': '''
El Segmento 3 corresponde a "Clientes Nuevos o Esporádicos".
Representa el 47% restante de la base.
Realizaron entre 1 y 2 compras en total, con ticket promedio de $210 MXN.
Alta variabilidad en categorías de producto — no tienen preferencia definida.
Baja tasa de devolución pero también baja recurrencia.
Recomendación: campaña de segundo-compra con incentivo de envío gratis
para convertirlos en clientes recurrentes antes de que abandonen definitivamente.
        '''
    },

    # --- MODELO SUPERVISADO (CHURN) ---
    {
        'id': 'churn_001',
        'categoria': 'Predicción de abandono',
        'titulo': 'Modelo de predicción de churn — Resultados generales',
        'contenido': '''
Se entrenó un modelo de clasificación Random Forest para predecir si un cliente
abandonará la plataforma en los próximos 30 días.
El modelo fue evaluado con las siguientes métricas en el conjunto de prueba:
- ROC-AUC: 0.87 (excelente capacidad de discriminación)
- Precisión: 0.82
- Recall: 0.79
- F1-Score: 0.80
Se analizó el sobreajuste comparando métricas en entrenamiento vs prueba;
la diferencia fue menor al 4%, lo que indica un modelo bien generalizado.
Las variables más importantes para predecir el abandono fueron:
1. Días desde la última compra (recencia)
2. Número de devoluciones en los últimos 60 días
3. Calificación promedio de satisfacción
4. Cambio en frecuencia de compra (últimos 30 vs 90 días)
        '''
    },
    {
        'id': 'churn_002',
        'categoria': 'Predicción de abandono',
        'titulo': 'Clientes con mayor riesgo de abandono',
        'contenido': '''
El modelo identificó que el 28% de los clientes activos tienen una probabilidad
de abandono superior al 70% en los próximos 30 días.
De estos clientes en riesgo alto:
- El 68% pertenece al Segmento 2 (Clientes en Riesgo)
- El 21% pertenece al Segmento 3 (Clientes Esporádicos)
- El 11% es preocupante: son clientes del Segmento VIP con señales de alerta
El perfil típico del cliente en riesgo alto es: sin compra en más de 45 días,
realizó al menos una devolución reciente, y su última calificación fue 2 o 3 estrellas.
Para Laura Martínez, la acción inmediata recomendada es contactar prioritariamente
al 11% de clientes VIP en riesgo, ya que representan el mayor impacto económico potencial.
        '''
    },

    # --- SERIES DE TIEMPO ---
    {
        'id': 'series_001',
        'categoria': 'Tendencias de ventas',
        'titulo': 'Análisis de tendencia de ventas 2020–2026',
        'contenido': '''
El análisis de series de tiempo de las ventas mensuales entre 2020 y 2026 revela
tres patrones importantes:
1. TENDENCIA GENERAL: Crecimiento sostenido del 12% anual promedio,
   con una caída temporal en 2022 relacionada con cambios en la cadena de suministro.
2. ESTACIONALIDAD: Picos claros en noviembre-diciembre (temporada navideña, +45%)
   y febrero (San Valentín, +18%). Valles en enero y julio.
3. PRONÓSTICO 2026: El modelo proyecta que mayo-agosto 2026 mantendrá
   un volumen de ventas estable, con crecimiento moderado del 8% vs el mismo
   periodo de 2025. El tercer trimestre será clave para preparar inventario
   para la temporada navideña.
Recomendación: La campaña de retención de mayo 2026 se ejecuta en un periodo
de ventas moderado, lo cual es ideal para reactivar clientes dormidos antes
de que llegue la temporada alta.
        '''
    },
    {
        'id': 'series_002',
        'categoria': 'Tendencias de ventas',
        'titulo': 'Categorías de producto con mejor y peor desempeño',
        'contenido': '''
El análisis de ventas por categoría de producto muestra:
CATEGORÍAS EN CRECIMIENTO (últimos 12 meses):
- Electrónica: +22% YoY, mayor ticket promedio
- Ropa y accesorios: +15% YoY, mayor volumen de transacciones
- Hogar y jardín: +11% YoY, frecuencia de compra más alta
CATEGORÍAS EN DECLIVE:
- Libros y medios físicos: -8% YoY
- Artículos deportivos: -3% YoY
La categoría de Electrónica concentra al 60% de los clientes VIP.
Los clientes del Segmento 2 (en riesgo) compraban principalmente en Ropa,
lo que sugiere que las campañas de retención deben incluir ofertas en esa categoría.
        '''
    },

    # --- HALLAZGOS INTEGRADOS ---
    {
        'id': 'hallazgos_001',
        'categoria': 'Hallazgos ejecutivos',
        'titulo': 'Resumen ejecutivo — Decisiones recomendadas',
        'contenido': '''
Con base en el análisis completo de Machine Learning, se presentan las siguientes
recomendaciones concretas para Laura Martínez, Gerente de Marketing de RetailMex:

ACCIÓN INMEDIATA (semana 1 de mayo 2026):
Contactar a los 11% de clientes VIP con señales de riesgo. Ofrecerles
atención personalizada y beneficios exclusivos. Presupuesto estimado: alto impacto.

ACCIÓN A 2 SEMANAS:
Lanzar campaña de descuento del 20% en categoría Ropa para clientes del
Segmento 2. Son el grupo más grande en riesgo y la categoría que prefieren.

ACCIÓN A 1 MES:
Programa de segunda compra para Segmento 3. Incentivo: envío gratis.
Objetivo: convertir al 25% de estos clientes en recurrentes antes de julio.

MÉTRICA DE ÉXITO:
Reducir la tasa de abandono mensual del 28% actual a menos del 20% para julio 2026.
        '''
    }
]

print(f' Base de conocimientos cargada: {len(documentos_conocimiento)} documentos')
print('Categorías disponibles:')
for cat in set(d['categoria'] for d in documentos_conocimiento):
    print(f'  • {cat}')





import chromadb
from chromadb.utils import embedding_functions
import time

# Usar sentence-transformers en español (gratuito, sin API key)
print(' Cargando modelo de embeddings (puede tardar 1-2 min la primera vez)...')
emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name='paraphrase-multilingual-MiniLM-L12-v2'  # Modelo multilingüe español/inglés
)

# Crear cliente ChromaDB en memoria
client = chromadb.Client()

# Crear o recuperar colección
collection = client.get_or_create_collection(
    name='ecommerce_hallazgos',
    embedding_function=emb_fn,
    metadata={'descripcion': 'Hallazgos ML del proyecto e-commerce 2020-2026'}
)

# Indexar todos los documentos
print(' Indexando documentos en la base vectorial...')
ids = [d['id'] for d in documentos_conocimiento]
textos = [d['titulo'] + '\n' + d['contenido'] for d in documentos_conocimiento]
metadatas = [{'categoria': d['categoria'], 'titulo': d['titulo']} for d in documentos_conocimiento]

collection.add(
    ids=ids,
    documents=textos,
    metadatas=metadatas
)

print(f' Base vectorial lista — {collection.count()} documentos indexados')


def recuperar_contexto(pregunta: str, n_resultados: int = 3) -> list:
    """Recupera los documentos más relevantes para una pregunta."""
    resultados = collection.query(
        query_texts=[pregunta],
        n_results=n_resultados
    )
    docs_recuperados = []
    for i, doc in enumerate(resultados['documents'][0]):
        docs_recuperados.append({
            'contenido': doc,
            'categoria': resultados['metadatas'][0][i]['categoria'],
            'titulo': resultados['metadatas'][0][i]['titulo'],
            'distancia': resultados['distances'][0][i]
        })
    return docs_recuperados

# Prueba rápida del retriever
test = recuperar_contexto('¿Qué clientes tienen mayor riesgo de abandono?')
print(f' Retriever funcionando — Recuperó {len(test)} documentos relevantes')
print(f'   Más relevante: "{test[0]["titulo"]}"')

gem_api_key = 'AIzaSyC4VYWAgwmp-eoXB4tJfMSDArLmN5E7fbc' 


import google.generativeai as genai
genai.configure(api_key=gem_api_key)

def generar_respuesta(pregunta: str, contexto_docs: list) -> str:
    """Genera una respuesta usando el LLM con el contexto recuperado."""
    # Formatear contexto
    contexto_texto = '\n\n---\n\n'.join([
        f"FUENTE: {d['titulo']} (Categoría: {d['categoria']})\n{d['contenido']}"
        for d in contexto_docs
    ])

    mensaje_usuario = f"""CONTEXTO DEL ANÁLISIS:
    {contexto_texto}

    PREGUNTA DE NEGOCIO:
    {pregunta}

    Responde basándote ÚNICAMENTE en el contexto proporcionado. Indica al final las fuentes usadas.
    Rol: Eres un asistente de análisis de datos para RetailMex, empresa de e-commerce.Tu rol es responder preguntas de negocio de Laura Martínez, Gerente de Marketing.

    REGLAS ESTRICTAS:
    1. Solo responde con información que esté en el CONTEXTO proporcionado.
    2. Si la información no está en el contexto, di exactamente: "Esta información no está disponible en el análisis realizado."
    3. Siempre indica la fuente de tu respuesta (nombre del documento).
    4. Usa lenguaje ejecutivo, claro y orientado a decisiones.
    5. Sé conciso: máximo 4 párrafos por respuesta.
    6. Nunca inventes números, porcentajes o afirmaciones que no estén en el contexto."""

    try:
        model = genai.GenerativeModel(model_name='models/gemini-2.5-flash')
        response = model.generate_content(
            contents=[
                {
                    "role": "user",
                    "parts": [
                        {"text": mensaje_usuario},
                    ],
                },
            ],

            )

        # Access the text from the response
        if response.candidates and response.candidates[0].content.parts:
            respuesta = response.candidates[0].content.parts[0].text
        else:
            respuesta = "No es posible responder esa pregunta."

    except Exception as e:
        respuesta = f"Error generating awnser: {e}"

    return respuesta


def rag_responder(pregunta: str, verbose: bool = True) -> dict:
    """
    Pipeline completo RAG:
    1. Recupera documentos relevantes
    2. Genera respuesta basada en evidencia
    3. Retorna respuesta + fuentes
    """
    if verbose:
        print(f'\n Buscando información relevante para: "{pregunta}"')

    # Recuperar contexto
    docs = recuperar_contexto(pregunta, n_resultados=3)

    if verbose:
        print(f' Documentos recuperados: {len(docs)}')
        for d in docs:
            print(f'   → {d["titulo"]}')
        print(' Generando respuesta...')

    # Generar respuesta
    respuesta = generar_respuesta(pregunta, docs)

    return {
        'pregunta': pregunta,
        'respuesta': respuesta,
        'fuentes': [d['titulo'] for d in docs]
    }

print(' Pipeline RAG listo ')

import gradio as gr

async def interfaz_rag(pregunta: str):
    """Función que conecta Gradio con el pipeline RAG."""
    if not pregunta.strip():
        return 'Por favor escribe una pregunta.', ''

    try:
        resultado =rag_responder(pregunta, verbose=True)
        respuesta = resultado['respuesta']
        fuentes = '\n'.join([f'• {f}' for f in resultado['fuentes']])
        return respuesta, fuentes
    except Exception as e:
        return f'Error al procesar la pregunta: {str(e)}', ''

# Preguntas de ejemplo para el decisor
ejemplos = [
    ['¿Qué clientes tienen mayor riesgo de abandono?'],
    ['¿Qué segmento debo priorizar en la campaña de mayo?'],
    ['¿Cómo van las ventas para el resto del año?'],
    ['¿Qué características tienen los clientes VIP?'],
    ['¿Qué acciones concretas recomienda el análisis?'],
]

# Construir interfaz
with gr.Blocks(
    title='Asistente RetailMex — Análisis de Clientes',
    theme=gr.themes.Soft()
) as demo:

    gr.Markdown("""
    #  Asistente de Análisis — RetailMex
    **Consulta los resultados del análisis de Machine Learning en lenguaje natural.**

    > Este asistente solo responde con base en el análisis realizado sobre el dataset de comportamiento
    > de clientes 2020–2026. No genera información que no provenga del análisis.
    """)

    with gr.Row():
        with gr.Column(scale=2):
            txt_pregunta = gr.Textbox(
                label='Tu pregunta de negocio',
                placeholder='Ej: ¿Qué clientes tienen mayor riesgo de abandono?',
                lines=2
            )
            btn_preguntar = gr.Button(' Consultar al asistente', variant='primary')

        with gr.Column(scale=3):
            txt_respuesta = gr.Textbox(
                label='Respuesta del asistente',
                lines=8,
                interactive=False
            )
            txt_fuentes = gr.Textbox(
                label='Fuentes consultadas (de los resultados del análisis)',
                lines=3,
                interactive=False
            )

    gr.Examples(
        examples=ejemplos,
        inputs=txt_pregunta,
        label=' Preguntas de ejemplo'
    )

    btn_preguntar.click(
        fn=interfaz_rag,
        inputs=txt_pregunta,
        outputs=[txt_respuesta, txt_fuentes]
    )

demo.launch(share=True)  # share=True genera un link público temporal
print('\n Interfaz lanzada — Copia el link "Running on public URL" para compartir')

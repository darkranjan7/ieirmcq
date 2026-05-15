from reportlab.lib.pagesizes import A4
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, 
                                 PageBreak, HRFlowable, Table, TableStyle)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

# ─── Document Setup ───────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    "IER_Exam_Preparation_2026.pdf",
    pagesize=A4,
    rightMargin=1.8*cm, leftMargin=1.8*cm,
    topMargin=2*cm, bottomMargin=2*cm
)

styles = getSampleStyleSheet()

# Custom styles
BLUE     = colors.HexColor("#1a3c6e")
DARKBLUE = colors.HexColor("#0d2244")
ACCENT   = colors.HexColor("#2563eb")
LIGHT    = colors.HexColor("#eff6ff")
GREEN    = colors.HexColor("#166534")
LIGHTGRN = colors.HexColor("#dcfce7")
ORANGE   = colors.HexColor("#7c2d12")
LIGHTOR  = colors.HexColor("#fff7ed")
GREY     = colors.HexColor("#374151")
LGREY    = colors.HexColor("#f3f4f6")

title_style = ParagraphStyle("TitleStyle", parent=styles["Title"],
    fontSize=22, textColor=DARKBLUE, spaceAfter=6, alignment=TA_CENTER,
    fontName="Helvetica-Bold")

subtitle_style = ParagraphStyle("SubTitle", parent=styles["Normal"],
    fontSize=12, textColor=ACCENT, spaceAfter=4, alignment=TA_CENTER,
    fontName="Helvetica")

module_style = ParagraphStyle("Module", parent=styles["Heading1"],
    fontSize=14, textColor=colors.white, spaceBefore=14, spaceAfter=6,
    fontName="Helvetica-Bold", backColor=BLUE,
    borderPad=(6,6,6,6), leftIndent=0, borderRadius=4)

q_style = ParagraphStyle("Question", parent=styles["Normal"],
    fontSize=11.5, textColor=DARKBLUE, spaceBefore=10, spaceAfter=4,
    fontName="Helvetica-Bold", leftIndent=0)

ans_style = ParagraphStyle("Answer", parent=styles["Normal"],
    fontSize=10.5, textColor=GREY, spaceBefore=2, spaceAfter=4,
    fontName="Helvetica", leading=16, alignment=TA_JUSTIFY)

bullet_style = ParagraphStyle("Bullet", parent=styles["Normal"],
    fontSize=10.5, textColor=GREY, spaceBefore=1, spaceAfter=1,
    fontName="Helvetica", leftIndent=20, leading=16,
    bulletIndent=8)

example_style = ParagraphStyle("Example", parent=styles["Normal"],
    fontSize=10, textColor=GREEN, spaceBefore=4, spaceAfter=4,
    fontName="Helvetica-Oblique", leftIndent=12, leading=15,
    backColor=LIGHTGRN, borderPad=5)

tip_style = ParagraphStyle("Tip", parent=styles["Normal"],
    fontSize=10, textColor=ORANGE, spaceBefore=4, spaceAfter=4,
    fontName="Helvetica-Oblique", leftIndent=12, leading=15,
    backColor=LIGHTOR, borderPad=5)

code_style = ParagraphStyle("Code", parent=styles["Normal"],
    fontSize=9.5, textColor=colors.HexColor("#1e293b"), spaceBefore=2, spaceAfter=4,
    fontName="Courier", leftIndent=14, leading=14,
    backColor=LGREY, borderPad=4)

marks_3_style = ParagraphStyle("Marks3", parent=styles["Heading2"],
    fontSize=13, textColor=colors.white, spaceBefore=12, spaceAfter=6,
    fontName="Helvetica-Bold", backColor=colors.HexColor("#1d4ed8"),
    borderPad=(5,5,5,5))

marks_5_style = ParagraphStyle("Marks5", parent=styles["Heading2"],
    fontSize=13, textColor=colors.white, spaceBefore=12, spaceAfter=6,
    fontName="Helvetica-Bold", backColor=colors.HexColor("#7e22ce"),
    borderPad=(5,5,5,5))

# ─── Helper ───────────────────────────────────────────────────────────────────
def Q(num, text):
    return Paragraph(f"Q{num}. {text}", q_style)

def A(text):
    return Paragraph(text, ans_style)

def B(text):
    return Paragraph(f"• {text}", bullet_style)

def Ex(text):
    return Paragraph(f"<b>Example:</b> {text}", example_style)

def Tip(text):
    return Paragraph(f"<b>Remember:</b> {text}", tip_style)

def space(h=6):
    return Spacer(1, h)

def hr():
    return HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#cbd5e1"), spaceAfter=4, spaceBefore=4)

def section(title, color=BLUE):
    return Paragraph(title, module_style)

# ─── Content ──────────────────────────────────────────────────────────────────
story = []

# COVER PAGE
story.append(space(30))
story.append(Paragraph("Information Extraction & Retrieval", title_style))
story.append(Paragraph("PEC-CSD602C", subtitle_style))
story.append(space(8))
story.append(HRFlowable(width="60%", thickness=2, color=ACCENT, hAlign="CENTER"))
story.append(space(8))
story.append(Paragraph("Complete Exam Preparation Guide", subtitle_style))
story.append(Paragraph("Even Semester Exam 2026 — Hasan Sir's Suggestions", 
    ParagraphStyle("sub2", parent=subtitle_style, fontSize=11, textColor=GREY)))
story.append(space(12))

# info box
data = [
    ["Course Code", "PEC-CSD602C"],
    ["Exam", "Even Semester 2026"],
    ["Total Questions Covered", "40 (20 × 3-mark + 20 × 5-mark)"],
    ["Language", "Simple Indian English — Beginner Friendly"],
]
t = Table(data, colWidths=[5*cm, 10*cm])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (0,-1), LIGHT),
    ('BACKGROUND', (1,0), (1,-1), colors.white),
    ('TEXTCOLOR', (0,0), (-1,-1), DARKBLUE),
    ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
    ('FONTNAME', (1,0), (1,-1), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('ROWBACKGROUNDS', (0,0), (-1,-1), [LIGHT, colors.white]),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#93c5fd")),
    ('PADDING', (0,0), (-1,-1), 7),
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
]))
story.append(t)
story.append(space(16))
story.append(Paragraph("Best of Luck! You CAN do this! 💪", 
    ParagraphStyle("luck", parent=subtitle_style, fontSize=13, textColor=GREEN)))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# TABLE OF CONTENTS (simple)
# ══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("What's Inside This Guide", 
    ParagraphStyle("toc_title", parent=title_style, fontSize=17)))
story.append(space(8))
toc_items = [
    ("Part A — 3-Mark Questions (Q1–Q20)", "Short, to-the-point answers"),
    ("Q1", "Query Reformulation"),
    ("Q2", "Link Spam"),
    ("Q3", "Explicit vs Implicit Relevance Feedback"),
    ("Q4", "PageRank"),
    ("Q5", "k-NN vs SVM"),
    ("Q6", "Criticism of k-Means"),
    ("Q7", "Query Expansion Techniques"),
    ("Q8", "SVM for Text Classification"),
    ("Q9", "Feature Selection"),
    ("Q10","Stopword Removal & Query Expansion"),
    ("Q11","Web as a Graph"),
    ("Q12","Anchor Text in Web Search"),
    ("Q13","Vector Space Model"),
    ("Q14","TF-IDF"),
    ("Q15","Cosine Similarity"),
    ("Q16","Supervised vs Unsupervised Learning"),
    ("Q17","Naive Bayes Classification"),
    ("Q18","Inverted Index"),
    ("Q19","Precision & Recall"),
    ("Q20","Overfitting"),
    ("Part B — 5-Mark Questions (Q31–Q50)", "Detailed answers with examples"),
    ("Q31","Compression Techniques in IR"),
    ("Q32","Cosine Similarity in Classification & Clustering"),
    ("Q33","High-Dimensional Data — Curse of Dimensionality"),
    ("Q34","Tolerant Retrieval Techniques"),
    ("Q35","Inverted Indexing for Efficiency"),
    ("Q36","K-Means Clustering Step-by-Step"),
    ("Q37","DBSCAN Algorithm"),
    ("Q38","Inverted Index — Advantages"),
    ("Q39","Real-World Applications of Text Clustering"),
    ("Q40","Relevance Feedback"),
    ("Q41","Query Reformulation Types"),
    ("Q42","Rocchio Algorithm"),
    ("Q43","Components of a Web Search Engine"),
    ("Q44","VSM vs Probabilistic Model"),
    ("Q45","Term Weighting Schemes"),
    ("Q46","Normalization Techniques"),
    ("Q47","Challenges in Web Crawling"),
    ("Q48","Language Models in IR"),
    ("Q49","Naive Bayes Classifier — Detailed"),
    ("Q50","Feature Extraction Techniques"),
]
for item in toc_items:
    if item[0].startswith("Part"):
        story.append(Paragraph(item[0] + " — " + item[1],
            ParagraphStyle("toc_h", parent=ans_style, fontName="Helvetica-Bold", 
                           textColor=ACCENT, fontSize=11, spaceBefore=6)))
    else:
        story.append(Paragraph(f"  {item[0]}: {item[1]}", 
            ParagraphStyle("toc_i", parent=ans_style, fontSize=10, spaceBefore=1)))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
#  PART A  —  3-MARK QUESTIONS
# ══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("PART A — 3-Mark Questions", marks_3_style))
story.append(space(4))

# ── Q1 ────────────────────────────────────────────────────────────────────────
story.append(Q(1, "How does query reformulation improve search results?"))
story.append(A("When you search something on Google and the results are not good, you change your search words. That is called query reformulation — changing or improving the original query to get better results."))
story.append(A("<b>How it helps:</b>"))
story.append(B("It removes unclear or wrong words from the query."))
story.append(B("It adds related words so the search engine understands better."))
story.append(B("It uses user feedback to understand what was really needed."))
story.append(B("It expands short queries into more meaningful ones."))
story.append(Ex('User searches "apple" (fruit or company?). After reformulation → "Apple iPhone latest model" — now results are much better.'))
story.append(Tip("Query reformulation = fixing + improving your search query to get better, more relevant results."))
story.append(hr())

# ── Q2 ────────────────────────────────────────────────────────────────────────
story.append(Q(2, "What is link spam, and how do search engines combat it?"))
story.append(A("Link spam means creating fake or low-quality links just to trick search engines into giving a website a higher rank. Since PageRank gives more importance to pages with more links, spammers create many useless links to boost their site."))
story.append(A("<b>Types of link spam:</b>"))
story.append(B("Link farms — Groups of websites that all link to each other just to increase count."))
story.append(B("Hidden links — Links that are invisible to users but visible to search engines."))
story.append(B("Comment spam — Posting links in blog comments."))
story.append(A("<b>How search engines fight it:</b>"))
story.append(B("TrustRank — Give high importance only to trusted, well-known sites."))
story.append(B("NoFollow tag — Tells search engine to ignore a particular link."))
story.append(B("Spam detection algorithms — Detect unusual link patterns."))
story.append(B("Google's Penguin update — Penalizes websites using spammy links."))
story.append(Ex("A fake website gets 1000 links from spam blogs overnight. Google detects this unusual pattern and lowers its rank."))
story.append(hr())

# ── Q3 ────────────────────────────────────────────────────────────────────────
story.append(Q(3, "Differentiate between explicit and implicit relevance feedback."))
story.append(A("Relevance feedback is when users help the search system by telling it which results are useful."))
data = [
    ["Feature", "Explicit Feedback", "Implicit Feedback"],
    ["How collected?", "User directly tells the system", "System observes user behavior"],
    ["User effort", "High — user must act", "Low — automatic"],
    ["Example", "Clicking thumbs up/down", "Time spent on a page"],
    ["Accuracy", "More accurate", "Less accurate (guessed)"],
    ["Common use", "Library systems", "Google, YouTube"],
]
t = Table(data, colWidths=[3.5*cm, 6.5*cm, 6.5*cm])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), BLUE),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT]),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#93c5fd")),
    ('PADDING', (0,0), (-1,-1), 5),
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
]))
story.append(space(4))
story.append(t)
story.append(Tip("Explicit = User tells | Implicit = System guesses from behavior."))
story.append(hr())

# ── Q4 ────────────────────────────────────────────────────────────────────────
story.append(Q(4, "What is PageRank, and how does it work?"))
story.append(A("PageRank is an algorithm created by Google founders Larry Page and Sergey Brin. It decides how important a webpage is based on how many other pages link to it. More links = more important page."))
story.append(A("<b>Simple idea:</b> A webpage is important if many important pages link to it. It's like getting a recommendation from a famous person — that means more than a recommendation from an unknown person."))
story.append(A("<b>Formula (simple form):</b>"))
story.append(Paragraph("PR(A) = (1 - d) + d × (sum of PR(B)/L(B) for each page B linking to A)", 
    code_style))
story.append(A("Where d = damping factor (usually 0.85), L(B) = number of outgoing links from B."))
story.append(A("<b>Key points:</b>"))
story.append(B("Pages with more inbound links get higher PageRank."))
story.append(B("A link from a high-PR page is worth more than from a low-PR page."))
story.append(B("Calculated iteratively — runs many times until values stabilize."))
story.append(B("Damping factor (0.85) simulates a user randomly clicking links."))
story.append(Ex("Wikipedia has millions of links from other sites → very high PageRank → appears at top of search results."))
story.append(hr())

# ── Q5 ────────────────────────────────────────────────────────────────────────
story.append(Q(5, "Compare and contrast k-NN and Support Vector Machines (SVM) in text classification."))
data = [
    ["Feature", "k-NN (k-Nearest Neighbours)", "SVM (Support Vector Machine)"],
    ["Type", "Lazy learner (no training)", "Eager learner (needs training)"],
    ["How it works", "Finds k closest documents; majority class wins", "Finds best boundary line between classes"],
    ["Speed", "Slow at prediction time", "Fast at prediction time"],
    ["Memory", "Needs all training data in memory", "Only needs support vectors"],
    ["Works well", "Small datasets", "Large, high-dimensional data"],
    ["Noise handling", "Sensitive to noisy data", "Robust to noise"],
    ["Example use", "Document similarity search", "Spam email classification"],
]
t = Table(data, colWidths=[3*cm, 6.5*cm, 7*cm])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), BLUE),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,-1), 8.5),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT]),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#93c5fd")),
    ('PADDING', (0,0), (-1,-1), 4),
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
]))
story.append(space(4))
story.append(t)
story.append(Tip("SVM is generally better for text classification because text data is high-dimensional."))
story.append(hr())

# ── Q6 ────────────────────────────────────────────────────────────────────────
story.append(Q(6, "Criticize the effectiveness of k-Means clustering for document classification."))
story.append(A("k-Means is a popular clustering algorithm, but it has many weaknesses when used for document classification:"))
story.append(B("<b>You must choose k in advance:</b> You need to tell the algorithm how many clusters to make. But in real life, you don't know how many categories exist."))
story.append(B("<b>Sensitive to initial centers:</b> If the starting points (centroids) are chosen badly, results will be wrong. Different runs give different results."))
story.append(B("<b>Only works with numerical data:</b> Text must first be converted to vectors (like TF-IDF), which adds extra steps."))
story.append(B("<b>Assumes circular clusters:</b> k-Means assumes clusters are round-shaped. Text clusters can be any shape."))
story.append(B("<b>Affected by outliers:</b> One unusual document can pull the centroid away from the real center."))
story.append(B("<b>Hard clusters only:</b> A document belongs to exactly one cluster. But many documents can belong to multiple topics."))
story.append(Ex("If you have news articles about 'sports', 'technology', and 'politics', k-Means may mix sports and technology articles if initialized badly."))
story.append(Tip("Better alternatives: DBSCAN (handles irregular shapes), EM algorithm (soft clustering), Hierarchical clustering."))
story.append(hr())

# ── Q7 ────────────────────────────────────────────────────────────────────────
story.append(Q(7, "What are some common techniques used for query expansion?"))
story.append(A("Query expansion means adding more useful words to a search query to improve results. There are several ways to do this:"))
story.append(B("<b>Synonym expansion:</b> Add words with similar meaning using a thesaurus. Example: 'car' → also search 'automobile', 'vehicle'."))
story.append(B("<b>Relevance feedback (Rocchio algorithm):</b> User marks relevant documents → system extracts their important words → adds to query."))
story.append(B("<b>Pseudo relevance feedback:</b> Automatically assume top results are relevant → extract key terms → expand query (no user needed)."))
story.append(B("<b>WordNet / ontology-based expansion:</b> Use knowledge databases to find related words."))
story.append(B("<b>Query logs:</b> Use past successful queries from other users with similar intent."))
story.append(B("<b>Stemming & lemmatization:</b> Treat 'run', 'running', 'ran' as same word."))
story.append(Ex("Query: 'heart disease treatment'. After expansion → 'heart disease treatment cardiac therapy medicine cure'."))
story.append(hr())

# ── Q8 ────────────────────────────────────────────────────────────────────────
story.append(Q(8, "How does the Support Vector Machine (SVM) classify text documents?"))
story.append(A("SVM is a classification algorithm that finds the best separating line (called a hyperplane) between two classes. The goal is to maximize the gap (margin) between the two classes."))
story.append(A("<b>Step-by-step for text:</b>"))
story.append(B("Step 1: Convert each document to a vector using TF-IDF."))
story.append(B("Step 2: Each document becomes a point in high-dimensional space."))
story.append(B("Step 3: SVM finds the hyperplane that best separates classes (e.g., spam vs not-spam)."))
story.append(B("Step 4: The points closest to the boundary are called Support Vectors."))
story.append(B("Step 5: New documents are classified based on which side of the hyperplane they fall."))
story.append(A("<b>For multiple classes:</b> Use one-vs-rest approach (e.g., 'sports vs all', 'politics vs all')."))
story.append(A("<b>Kernel trick:</b> When data is not linearly separable, SVM uses kernel functions (RBF, polynomial) to map data to higher dimension where separation is possible."))
story.append(Ex("Email spam classification: SVM learns the boundary between spam and non-spam emails. New email → convert to vector → check which side of boundary → classify."))
story.append(hr())

# ── Q9 ────────────────────────────────────────────────────────────────────────
story.append(Q(9, "What is feature selection in text classification, and why is it important?"))
story.append(A("In text classification, a document can have thousands of words (features). Feature selection is the process of choosing only the most useful words/features and removing the less useful ones."))
story.append(A("<b>Why it is important:</b>"))
story.append(B("Reduces computation time — fewer features = faster training."))
story.append(B("Reduces noise — removing irrelevant words improves accuracy."))
story.append(B("Prevents overfitting — model does not memorize unnecessary words."))
story.append(B("Saves memory — smaller feature space."))
story.append(A("<b>Common techniques:</b>"))
story.append(B("Document Frequency (DF): Remove words that appear in too few or too many documents."))
story.append(B("Information Gain (IG): Keep words that give the most information about the class."))
story.append(B("Chi-square test: Statistical test to find words strongly associated with a class."))
story.append(B("Mutual Information: Measures dependency between word and class."))
story.append(B("Term Frequency thresholding: Remove very rare words."))
story.append(Ex("In spam detection, words like 'lottery', 'winner', 'free money' are highly informative features. Words like 'the', 'is', 'a' are not useful — they are removed."))
story.append(hr())

# ── Q10 ───────────────────────────────────────────────────────────────────────
story.append(Q(10, "What is the impact of stopword removal on query expansion?"))
story.append(A("Stopwords are very common words like 'the', 'is', 'and', 'a', 'in' that carry almost no meaning. Removing them is a standard step in IR. But it has mixed impact on query expansion:"))
story.append(A("<b>Positive impacts:</b>"))
story.append(B("Reduces query size — expansion becomes more focused on meaningful words."))
story.append(B("Better matching — important terms get more weight."))
story.append(B("Saves processing time."))
story.append(A("<b>Negative impacts:</b>"))
story.append(B("Some queries lose meaning — Example: 'to be or not to be' (Shakespeare quote) — removing stopwords leaves nothing useful."))
story.append(B("Phrase-based queries suffer — 'flights to Delhi' becomes 'flights Delhi' — meaning changes slightly."))
story.append(B("Can hurt precision in some cases when position/context matters."))
story.append(Ex("Query: 'What is the capital of India?' → After stopword removal → 'capital India' → query expansion adds 'capital city Delhi India government' → better results."))
story.append(Tip("Stopword removal generally HELPS query expansion but must be used carefully for short, specific queries."))
story.append(hr())

# ── Q11 ───────────────────────────────────────────────────────────────────────
story.append(Q(11, "Explain the structure of the web as a graph."))
story.append(A("The World Wide Web can be modeled as a directed graph where:"))
story.append(B("<b>Nodes</b> = Web pages"))
story.append(B("<b>Edges</b> = Hyperlinks (directed — from one page to another)"))
story.append(A("If page A has a link to page B, then there is a directed edge from A → B."))
story.append(A("<b>Bow-Tie Structure of the Web:</b> Research found the web looks like a 'bow-tie':"))
story.append(B("<b>SCC (Strongly Connected Core):</b> Central core — large group of pages all reachable from each other (~28% of web)."))
story.append(B("<b>IN component:</b> Pages that link INTO the core but cannot be reached from core."))
story.append(B("<b>OUT component:</b> Pages that can be reached FROM the core but don't link back."))
story.append(B("<b>Tendrils & Tubes:</b> Isolated pages connected loosely."))
story.append(A("<b>Properties of the Web Graph:</b>"))
story.append(B("Small-world property — Most pages are connected within a few hops."))
story.append(B("Power-law degree distribution — Few pages have millions of links; most have very few."))
story.append(Ex("Google.com is in the core — you can reach it from most pages and reach most pages from it. A small personal blog may be in the OUT section — you can reach it from the core but it doesn't link back."))
story.append(hr())

# ── Q12 ───────────────────────────────────────────────────────────────────────
story.append(Q(12, "Explain the role of anchor text in web search."))
story.append(A("Anchor text is the clickable visible text of a hyperlink. Example: in the link <u>Click here for weather</u>, the anchor text is 'Click here for weather'."))
story.append(A("<b>Why anchor text is important in web search:</b>"))
story.append(B("Describes the linked page — The anchor text often tells what the target page is about, even better than the page itself."))
story.append(B("Improves indexing — Search engines index anchor text to understand what a page contains."))
story.append(B("Boosts relevance — If 1000 pages link to a site with anchor text 'best biryani recipe', that site ranks high for 'biryani recipe'."))
story.append(B("Helps pages with little text — A page with few words can still be found if many pages link to it with relevant anchor text."))
story.append(A("<b>Anchor text in PageRank:</b> Not only the number of links matters — the words in the anchor text also affect ranking."))
story.append(Ex("Wikipedia pages rank high in searches because thousands of websites link to them using descriptive anchor text like 'history of India', 'photosynthesis explanation' etc."))
story.append(Tip("Anchor text is like a short review/label of the target page, written by the linking page's author."))
story.append(hr())

# ── Q13 ───────────────────────────────────────────────────────────────────────
story.append(Q(13, "What is the Vector Space Model, and how is it used in information retrieval?"))
story.append(A("The Vector Space Model (VSM) is a mathematical way to represent documents and queries as vectors (lists of numbers) in a multi-dimensional space. Each dimension represents a unique word (term) in the vocabulary."))
story.append(A("<b>How it works:</b>"))
story.append(B("Step 1: Build a vocabulary of all unique words from all documents."))
story.append(B("Step 2: Represent each document as a vector — each position = weight of a term (usually TF-IDF weight)."))
story.append(B("Step 3: Represent the query also as a vector."))
story.append(B("Step 4: Calculate similarity between query vector and each document vector (cosine similarity)."))
story.append(B("Step 5: Rank documents by similarity score — highest similarity = most relevant."))
story.append(Ex("Documents: D1='cat dog', D2='cat fish'. Query='cat'. In VSM, D1 and D2 are represented as vectors. Query vector is compared to both. Closest document is returned as most relevant."))
story.append(A("<b>Advantages:</b> Handles partial matching, gives ranked results, easy to compute."))
story.append(A("<b>Limitations:</b> Ignores word order, assumes independence between terms."))
story.append(hr())

# ── Q14 ───────────────────────────────────────────────────────────────────────
story.append(Q(14, "Define TF-IDF and explain its significance in text processing."))
story.append(A("TF-IDF stands for Term Frequency - Inverse Document Frequency. It is a numerical weight given to each word in a document to show how important that word is."))
story.append(A("<b>TF (Term Frequency):</b> How many times a word appears in a document."))
story.append(Paragraph("TF(t,d) = (Number of times term t appears in document d) / (Total terms in d)", code_style))
story.append(A("<b>IDF (Inverse Document Frequency):</b> How rare a word is across all documents. Rare words are more informative."))
story.append(Paragraph("IDF(t) = log(Total documents / Documents containing term t)", code_style))
story.append(A("<b>TF-IDF = TF × IDF</b>"))
story.append(A("<b>Significance:</b>"))
story.append(B("Common words like 'the', 'is' get very low TF-IDF (because IDF is low — they appear everywhere)."))
story.append(B("Important topic-specific words get high TF-IDF."))
story.append(B("Used in VSM to build document vectors."))
story.append(B("Helps search engines rank documents."))
story.append(Ex("In a document about cricket: Word 'cricket' has high TF-IDF. Word 'the' has low TF-IDF. So 'cricket' is identified as the key topic word."))
story.append(Tip("TF = importance in THIS document | IDF = rarity ACROSS documents | Together they find truly important words."))
story.append(hr())

# ── Q15 ───────────────────────────────────────────────────────────────────────
story.append(Q(15, "What is cosine similarity, and how is it applied in document ranking?"))
story.append(A("Cosine similarity measures the similarity between two vectors by computing the cosine of the angle between them. Value is between 0 and 1. Value 1 = identical direction (very similar), Value 0 = perpendicular (no similarity)."))
story.append(Paragraph("cosine_sim(A, B) = (A · B) / (|A| × |B|)  =  dot product / product of magnitudes", code_style))
story.append(A("<b>Why cosine and not just dot product?</b> Cosine normalizes for document length — a longer document has more words, so dot product alone would unfairly favor it. Cosine removes this bias."))
story.append(A("<b>How it is used in document ranking:</b>"))
story.append(B("Convert query and all documents into TF-IDF vectors."))
story.append(B("Calculate cosine similarity between query vector and each document vector."))
story.append(B("Rank documents from highest to lowest similarity."))
story.append(B("Top results are shown to the user."))
story.append(Ex("Query vector: [0.5, 0.3, 0] for words (cricket, bat, movie). Doc1: [0.6, 0.4, 0.1], Doc2: [0.1, 0.1, 0.9]. Cosine with Doc1 is much higher → Doc1 is more relevant to cricket query."))
story.append(hr())

# ── Q16 ───────────────────────────────────────────────────────────────────────
story.append(Q(16, "Differentiate between supervised and unsupervised learning in text mining."))
data = [
    ["Feature", "Supervised Learning", "Unsupervised Learning"],
    ["Labeled data?", "Yes — data has predefined labels", "No — data has no labels"],
    ["Goal", "Learn to predict labels for new data", "Discover hidden patterns/groups"],
    ["Algorithms", "Naive Bayes, SVM, k-NN, Decision Tree", "k-Means, DBSCAN, Hierarchical"],
    ["Task type", "Classification", "Clustering"],
    ["Example", "Email spam detection (spam/not-spam)", "Grouping news articles by topic"],
    ["Output", "Predefined categories", "Unknown groups discovered"],
    ["Human effort", "High (labeling training data)", "Low (no labeling needed)"],
]
t = Table(data, colWidths=[3.2*cm, 6.5*cm, 6.8*cm])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), BLUE),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT]),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#93c5fd")),
    ('PADDING', (0,0), (-1,-1), 5),
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
]))
story.append(space(4))
story.append(t)
story.append(hr())

# ── Q17 ───────────────────────────────────────────────────────────────────────
story.append(Q(17, "What is Naive Bayes classification, and how does it work for text data?"))
story.append(A("Naive Bayes is a simple and fast classification algorithm based on Bayes' Theorem. It is called 'Naive' because it assumes all words/features are independent of each other — which is a simplification, but it still works very well in practice."))
story.append(A("<b>Bayes' Theorem:</b>"))
story.append(Paragraph("P(Class | Document) = P(Document | Class) × P(Class) / P(Document)", code_style))
story.append(A("<b>How it works for text (spam detection example):</b>"))
story.append(B("Training: Calculate probability of each word appearing in spam and non-spam emails."))
story.append(B("For a new email, calculate P(spam | words in email) and P(not-spam | words in email)."))
story.append(B("Whichever probability is higher → that is the classification."))
story.append(A("<b>Key terms:</b>"))
story.append(B("Prior probability P(Class): How common is each class? Example: 40% emails are spam."))
story.append(B("Likelihood P(word|Class): How often does this word appear in spam?"))
story.append(B("Laplace smoothing: Add 1 to every word count to avoid zero probability for unseen words."))
story.append(Ex("Word 'lottery' appears 90% in spam, 2% in normal mail. If new email has 'lottery' → most likely spam."))
story.append(Tip("Naive Bayes is fast, works well with small training data, and great for text classification despite being 'naive'."))
story.append(hr())

# ── Q18 ───────────────────────────────────────────────────────────────────────
story.append(Q(18, "What are inverted indexes, and why are they important in search engines?"))
story.append(A("An inverted index is a data structure used by search engines to quickly find which documents contain a given word. It is the opposite of a forward index (which goes document → words). An inverted index goes word → documents."))
story.append(A("<b>Structure:</b>"))
story.append(Paragraph("Word  →  [Doc1, Doc2, Doc5, ...]  (list of document IDs where word appears)", code_style))
story.append(A("<b>Example:</b>"))
story.append(Paragraph(
    "cricket → [Doc1, Doc3, Doc7]\n"
    "bat     → [Doc1, Doc2, Doc7]\n"
    "football → [Doc2, Doc4]", code_style))
story.append(A("<b>Why important:</b>"))
story.append(B("Very fast search — Instead of reading all documents, just look up the word in the index."))
story.append(B("Boolean queries — For 'cricket AND bat', just intersect the two lists: [Doc1, Doc7]."))
story.append(B("Scalable — Works even for billions of documents like the web."))
story.append(B("Foundation of all modern search engines (Google, Bing, etc.)"))
story.append(Tip("Inverted index = Like the index at the back of a textbook — tells you which pages contain a word, without reading the whole book."))
story.append(hr())

# ── Q19 ───────────────────────────────────────────────────────────────────────
story.append(Q(19, "Explain precision and recall as evaluation metrics in information retrieval."))
story.append(A("Precision and Recall are two key metrics to evaluate how well an IR system is performing."))
story.append(Paragraph("Precision = Relevant documents retrieved / Total documents retrieved", code_style))
story.append(Paragraph("Recall    = Relevant documents retrieved / Total relevant documents in collection", code_style))
story.append(A("<b>Simple understanding:</b>"))
story.append(B("<b>Precision</b> = Of what the system returned, how much was actually useful? (Quality)"))
story.append(B("<b>Recall</b> = Of all useful documents, how many did the system find? (Coverage)"))
story.append(Ex("Collection has 10 relevant documents. System retrieves 8 documents total, of which 6 are relevant. Precision = 6/8 = 75%. Recall = 6/10 = 60%."))
story.append(A("<b>Trade-off:</b> Increasing precision usually decreases recall and vice versa. High precision = few but accurate results. High recall = finds everything but includes many irrelevant results."))
story.append(A("<b>F1-Score</b> = harmonic mean of both = 2×(P×R)/(P+R) — balances both."))
story.append(Tip("Precision = 'Are the results good?' | Recall = 'Did we find everything?'"))
story.append(hr())

# ── Q20 ───────────────────────────────────────────────────────────────────────
story.append(Q(20, "What is overfitting in machine learning, and how can it be avoided?"))
story.append(A("Overfitting happens when a machine learning model learns the training data TOO well — it memorizes even the noise and random patterns, so it performs perfectly on training data but very poorly on new, unseen data."))
story.append(A("<b>Simple analogy:</b> Imagine a student who memorizes every answer from last year's question paper. They fail completely when the exam has new questions."))
story.append(A("<b>Signs of overfitting:</b>"))
story.append(B("Very high accuracy on training data (e.g., 99%)."))
story.append(B("Very low accuracy on test/new data (e.g., 60%)."))
story.append(A("<b>How to avoid overfitting:</b>"))
story.append(B("Cross-validation — Test on different subsets of data during training."))
story.append(B("Regularization — Penalize complex models (L1/L2 regularization)."))
story.append(B("More training data — More data → model generalizes better."))
story.append(B("Feature selection — Remove irrelevant features."))
story.append(B("Pruning (in Decision Trees) — Remove unnecessary branches."))
story.append(B("Early stopping — Stop training before model starts memorizing."))
story.append(B("Dropout (in Neural Networks) — Randomly disable neurons during training."))
story.append(Ex("SVM with very complex kernel overfits spam dataset. Using simpler linear kernel reduces overfitting and gives better results on new emails."))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
#  PART B  —  5-MARK QUESTIONS
# ══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("PART B — 5-Mark Questions", marks_5_style))
story.append(space(4))

# ── Q31 ───────────────────────────────────────────────────────────────────────
story.append(Q(31, "What are the different types of compression techniques used in IR?"))
story.append(A("In IR, we need to store huge indexes efficiently. Compression reduces storage space and speeds up retrieval. There are two kinds: Dictionary compression and Postings list compression."))
story.append(A("<b>1. Dictionary Compression:</b>"))
story.append(B("<b>Fixed-width storage:</b> Each term gets same space (e.g., 20 bytes). Simple but wastes space for short words."))
story.append(B("<b>Dictionary-as-a-string:</b> All terms stored in one long string; use pointers to find each term. Saves wasted space."))
story.append(B("<b>Blocked storage:</b> Store every 4th term fully; use pointers to decode others. Reduces pointer overhead."))
story.append(B("<b>Front coding:</b> Store common prefix once, only unique suffix separately. Example: 'automate', 'automatic', 'automation' → store 'automat' + suffixes 'e', 'ic', 'ion'."))
story.append(A("<b>2. Postings List Compression:</b>"))
story.append(B("<b>Gap encoding (d-gaps):</b> Instead of storing actual doc IDs [3,7,12,19], store differences [3,4,5,7]. Small gaps = fewer bits needed."))
story.append(B("<b>Variable Byte (VB) Encoding:</b> Uses 7 bits for data, 1 bit to signal if more bytes follow. Works well for varied gap sizes."))
story.append(B("<b>Gamma encoding:</b> Uses fewer bits for small numbers. More efficient for frequently occurring terms."))
story.append(B("<b>Elias-Fano coding:</b> Efficient for sorted integer lists — used in modern search engines."))
story.append(Ex("Document IDs: [100, 200, 350, 400]. Gaps: [100, 100, 150, 50]. These smaller numbers compress better than original large IDs."))
story.append(Tip("Goal of compression: Smaller index = faster loading into memory = faster search."))
story.append(hr())

# ── Q32 ───────────────────────────────────────────────────────────────────────
story.append(Q(32, "How does cosine similarity help in text classification and clustering?"))
story.append(A("Cosine similarity is a measure of how similar two vectors are, based on the angle between them. In both classification and clustering, we first represent each document as a TF-IDF vector, then use cosine similarity to compare them."))
story.append(A("<b>In Text Classification (k-NN):</b>"))
story.append(B("New document → convert to vector."))
story.append(B("Calculate cosine similarity with all training documents."))
story.append(B("Find k most similar documents (k-nearest neighbors)."))
story.append(B("Majority class among those k documents = predicted class."))
story.append(Ex("New document is about 'cricket'. It has high cosine similarity with documents labeled 'sports'. → Classified as 'sports'."))
story.append(A("<b>In Text Clustering (k-Means):</b>"))
story.append(B("Documents are grouped by their cosine similarity with cluster centroids."))
story.append(B("Documents more similar to centroid C1 than C2 are placed in cluster 1."))
story.append(B("Cosine similarity is preferred over Euclidean distance for text because text vectors are sparse and high-dimensional — Euclidean distance is misleading in such spaces."))
story.append(Ex("10 news articles on cricket and 10 on movies. After k-Means with cosine similarity, articles naturally group into 2 clusters based on content."))
story.append(A("<b>Advantages of cosine similarity for text:</b>"))
story.append(B("Length-independent — A short article and a long article on the same topic will still be similar."))
story.append(B("Works well with sparse TF-IDF vectors."))
story.append(B("Computationally efficient."))
story.append(hr())

# ── Q33 ───────────────────────────────────────────────────────────────────────
story.append(Q(33, "Discuss the impact of high-dimensional data in text classification and clustering. How can it be reduced?"))
story.append(A("In text mining, each unique word in the vocabulary is a feature (dimension). A vocabulary of 100,000 words means each document is a 100,000-dimensional vector. This is called the 'Curse of Dimensionality' and causes many problems."))
story.append(A("<b>Problems caused by high dimensionality:</b>"))
story.append(B("<b>Sparsity:</b> Most document vectors are almost all zeros (most words don't appear in a given document). This makes distance calculations less meaningful."))
story.append(B("<b>Overfitting:</b> Too many features → model learns noise → poor performance on new data."))
story.append(B("<b>Slow computation:</b> More features = more memory and processing time."))
story.append(B("<b>Distance meaninglessness:</b> In high dimensions, all points seem equally far from each other — making clustering unreliable."))
story.append(A("<b>Dimensionality Reduction Techniques:</b>"))
story.append(B("<b>Feature Selection:</b> Remove rare words, stopwords, irrelevant terms using methods like Information Gain, Chi-square."))
story.append(B("<b>Principal Component Analysis (PCA):</b> Finds new axes (principal components) that capture most variance. Projects data to fewer dimensions."))
story.append(B("<b>Latent Semantic Analysis (LSA/LSI):</b> Uses SVD (Singular Value Decomposition) to find hidden topic structure. Reduces thousands of words to ~300 topic dimensions."))
story.append(B("<b>Word Embeddings (Word2Vec, GloVe):</b> Map each word to a dense low-dimensional vector (e.g., 300 dimensions) capturing semantic meaning."))
story.append(B("<b>Random Projections:</b> Randomly project to lower dimensions while preserving distances approximately (Johnson-Lindenstrauss lemma)."))
story.append(Ex("50,000-word vocabulary → after removing stopwords and rare words → 10,000 words → after LSA → 300 topic dimensions. Same data, much less computation, often better accuracy."))
story.append(hr())

# ── Q34 ───────────────────────────────────────────────────────────────────────
story.append(Q(34, "What is tolerant retrieval in IR? Discuss different tolerant retrieval techniques."))
story.append(A("Standard retrieval requires an exact match between query terms and index terms. Tolerant retrieval handles situations where the query word doesn't exactly match the indexed word — due to spelling mistakes, variations, or different forms of the same word."))
story.append(A("<b>Why needed?</b> Users make spelling errors, use different spellings (colour/color), abbreviations, or similar-sounding words."))
story.append(A("<b>Techniques:</b>"))
story.append(B("<b>1. Wildcard queries:</b> Use * to match any sequence of characters. Example: 'mon*' matches 'money', 'monkey', 'monitor'. Implemented using permuterm index or k-gram index."))
story.append(B("<b>2. k-gram index:</b> Break words into overlapping k-grams (sequences of k characters). Example: 'castle' with k=2 → 'ca', 'as', 'st', 'tl', 'le'. Match query k-grams with document k-grams."))
story.append(B("<b>3. Edit Distance (Levenshtein Distance):</b> Measure how many single-character changes (insert, delete, substitute) are needed to convert one word to another. 'kitten' → 'sitting' = 3 edits."))
story.append(B("<b>4. Phonetic indexing (Soundex):</b> Index words by how they sound. 'Smith' and 'Smyth' sound the same → same Soundex code → matched together."))
story.append(B("<b>5. Stemming:</b> Reduce words to root form. 'running', 'runs', 'ran' → 'run'. Then match root forms."))
story.append(B("<b>6. Lemmatization:</b> Like stemming but linguistically correct. 'better' → 'good', 'are' → 'be'."))
story.append(Ex("User types 'restarant' (typo for 'restaurant'). Edit distance = 1. System returns results for 'restaurant' — user gets correct results despite the typo."))
story.append(hr())

# ── Q35 ───────────────────────────────────────────────────────────────────────
story.append(Q(35, "Explain how inverted indexing improves the efficiency of retrieval models."))
story.append(A("An inverted index maps each term to the list of documents containing it. This dramatically improves retrieval speed compared to scanning all documents for each query."))
story.append(A("<b>Without inverted index (naive approach):</b>"))
story.append(B("For each query, read every document and check if the query word is present."))
story.append(B("Time complexity: O(N × L) where N = total documents, L = average document length."))
story.append(B("For a web-scale collection (billions of pages), this is completely impractical."))
story.append(A("<b>With inverted index:</b>"))
story.append(B("Query word → look up index → instantly get list of relevant document IDs."))
story.append(B("Time complexity: O(k) where k = number of documents containing the term."))
story.append(B("Boolean AND → intersect two lists → fast skip-pointers make this even faster."))
story.append(A("<b>Additional efficiency features:</b>"))
story.append(B("<b>Skip pointers:</b> Jump ahead in posting lists during intersection — O(log N) instead of O(N)."))
story.append(B("<b>Sorted posting lists:</b> Easier and faster to merge/intersect."))
story.append(B("<b>Compression:</b> Compressed posting lists fit in RAM → even faster access."))
story.append(B("<b>Caching:</b> Popular terms' posting lists cached in memory."))
story.append(B("<b>Tiered indexes:</b> Separate indexes for different term frequencies for even faster top-k retrieval."))
story.append(Ex("Google indexes trillions of pages. When you search 'Dosa recipe', it looks up 'Dosa' and 'recipe' in the index and intersects the lists in milliseconds — without reading a single webpage."))
story.append(hr())

# ── Q36 ───────────────────────────────────────────────────────────────────────
story.append(Q(36, "Explain the K-Means clustering algorithm with a step-by-step example."))
story.append(A("K-Means is an iterative unsupervised clustering algorithm that partitions n data points into k clusters. Each point belongs to the cluster with the nearest centroid (mean)."))
story.append(A("<b>Algorithm Steps:</b>"))
story.append(B("<b>Step 1 — Choose k:</b> Decide number of clusters. Say k=2."))
story.append(B("<b>Step 2 — Initialize centroids:</b> Randomly pick k data points as initial centroids."))
story.append(B("<b>Step 3 — Assignment:</b> Assign each data point to nearest centroid (using cosine similarity or Euclidean distance)."))
story.append(B("<b>Step 4 — Update centroids:</b> Recalculate each centroid as the mean of all points assigned to it."))
story.append(B("<b>Step 5 — Repeat:</b> Repeat steps 3-4 until centroids don't change (convergence) or max iterations reached."))
story.append(A("<b>Step-by-Step Example (with documents):</b>"))
story.append(Paragraph(
    "Documents:\n"
    "  D1: 'cricket bat ball'     D2: 'cricket match IPL'\n"
    "  D3: 'movie actor cinema'   D4: 'film director award'\n\n"
    "k=2. Initial centroids: C1=D1, C2=D3\n\n"
    "Iteration 1 - Assignment:\n"
    "  D1 → C1 (cricket content), D2 → C1 (cricket content)\n"
    "  D3 → C2 (movie content),   D4 → C2 (movie content)\n\n"
    "Iteration 1 - Update:\n"
    "  C1 = mean(D1, D2), C2 = mean(D3, D4)\n\n"
    "Iteration 2: Same assignments → CONVERGED!\n"
    "Result: Cluster1={D1,D2} (Sports), Cluster2={D3,D4} (Movies)", code_style))
story.append(A("<b>Convergence:</b> Algorithm converges when no point changes its cluster. This is guaranteed but may reach local minimum, not global."))
story.append(A("<b>Choosing k:</b> Use the Elbow method — plot error vs k, find the 'elbow' point."))
story.append(hr())

# ── Q37 ───────────────────────────────────────────────────────────────────────
story.append(Q(37, "Explain the working principle of the DBSCAN clustering algorithm and its advantages over K-Means."))
story.append(A("DBSCAN (Density-Based Spatial Clustering of Applications with Noise) is a clustering algorithm that finds clusters based on density — areas where many points are close together."))
story.append(A("<b>Key Parameters:</b>"))
story.append(B("<b>Epsilon (ε):</b> Maximum radius — how far to look for neighbors."))
story.append(B("<b>MinPts:</b> Minimum number of points needed to form a dense region."))
story.append(A("<b>Point Types:</b>"))
story.append(B("<b>Core point:</b> Has at least MinPts neighbors within radius ε."))
story.append(B("<b>Border point:</b> Is neighbor of a core point but has fewer than MinPts neighbors itself."))
story.append(B("<b>Noise point (outlier):</b> Is neither a core nor border point."))
story.append(A("<b>Algorithm:</b>"))
story.append(B("Step 1: Pick an unvisited point."))
story.append(B("Step 2: Find all neighbors within radius ε."))
story.append(B("Step 3: If neighbors ≥ MinPts → mark as core point → expand cluster by visiting all neighbors."))
story.append(B("Step 4: If neighbors < MinPts → mark as noise (may be reassigned later as border point)."))
story.append(B("Step 5: Repeat until all points visited."))
story.append(A("<b>Advantages over K-Means:</b>"))
story.append(B("No need to specify k (number of clusters) in advance."))
story.append(B("Can find clusters of ANY shape (not just circular)."))
story.append(B("Automatically identifies and ignores outliers/noise."))
story.append(B("Works well for geographic data and irregular text clusters."))
story.append(Ex("Customer complaints dataset: DBSCAN finds 3 groups — billing issues (dense), delivery issues (dense), and 5 random complaints (noise). K-Means would force all 5 noise points into a cluster."))
story.append(hr())

# ── Q38 ───────────────────────────────────────────────────────────────────────
story.append(Q(38, "What is an inverted index? Explain its advantages in text retrieval."))
story.append(A("An inverted index is a mapping from terms (words) to the documents that contain them. It is the core data structure behind all modern search engines."))
story.append(A("<b>Structure of inverted index:</b>"))
story.append(Paragraph(
    "Term         | Document Frequency | Postings List\n"
    "-------------|-------------------|---------------------------\n"
    "cricket      |        5          | [D1, D3, D7, D9, D12]\n"
    "bat          |        3          | [D1, D3, D9]\n"
    "movie        |        4          | [D2, D5, D8, D11]", code_style))
story.append(A("Each entry also stores the term's position within each document (for phrase queries)."))
story.append(A("<b>Advantages:</b>"))
story.append(B("<b>Extremely fast lookup:</b> Finding all documents with word 'cricket' takes O(1) — just look up the hash table."))
story.append(B("<b>Boolean query processing:</b> AND → intersect lists, OR → union lists, NOT → complement. All can be done quickly on sorted lists."))
story.append(B("<b>Phrase queries:</b> Position information allows exact phrase matching."))
story.append(B("<b>Ranked retrieval:</b> Stores term frequency (TF) for each doc — enables TF-IDF computation."))
story.append(B("<b>Scalability:</b> Can be distributed across multiple machines (like Google's system)."))
story.append(B("<b>Compressed storage:</b> Using gap encoding, the index fits in limited memory."))
story.append(B("<b>Incremental updates:</b> New documents can be added without rebuilding entire index."))
story.append(hr())

# ── Q39 ───────────────────────────────────────────────────────────────────────
story.append(Q(39, "What are some real-world applications of text clustering? Provide examples."))
story.append(A("Text clustering automatically groups similar text documents together without requiring labeled data. Here are important real-world applications:"))
story.append(B("<b>1. News Article Organization:</b> Google News automatically groups news articles about the same event from different sources. Example: All articles about 'India vs Pakistan match' are grouped together."))
story.append(B("<b>2. Customer Feedback Analysis:</b> E-commerce companies (Amazon, Flipkart) cluster thousands of customer reviews into groups like 'delivery issues', 'quality problems', 'packaging feedback'. Helps identify major pain points."))
story.append(B("<b>3. Email Management:</b> Gmail clusters emails into categories — Primary, Social, Promotions — using text clustering techniques."))
story.append(B("<b>4. Search Result Organization:</b> Search engines cluster results to show different perspectives. For query 'Java', clusters might be: 'Java programming language', 'Java island Indonesia', 'Java coffee'."))
story.append(B("<b>5. Medical Record Analysis:</b> Hospital records clustered by symptoms, diagnoses to find patterns in diseases. Helps in epidemic detection."))
story.append(B("<b>6. Social Media Monitoring:</b> Cluster tweets/posts about a brand to find sentiment trends and issues. Companies use this for reputation management."))
story.append(B("<b>7. Document Recommendation:</b> Research paper recommendation systems — find papers similar to what you're reading using text clustering."))
story.append(B("<b>8. Plagiarism Detection:</b> Cluster documents by similarity — if two documents are in same cluster with very high similarity, possible plagiarism."))
story.append(B("<b>9. Chatbot Training:</b> Cluster user questions to identify common intents and train chatbots."))
story.append(Ex("Swiggy/Zomato clusters user complaints into 'late delivery', 'wrong order', 'quality issue' to route them to appropriate teams automatically."))
story.append(hr())

# ── Q40 ───────────────────────────────────────────────────────────────────────
story.append(Q(40, "Explain relevance feedback and its role in improving search results."))
story.append(A("Relevance feedback is an interactive process where the search system learns from the user's response to initial results to improve subsequent results."))
story.append(A("<b>Basic Process:</b>"))
story.append(B("Step 1: User submits initial query."))
story.append(B("Step 2: System returns initial results."))
story.append(B("Step 3: User marks which results are relevant and which are not."))
story.append(B("Step 4: System reformulates query based on this feedback."))
story.append(B("Step 5: System returns improved results."))
story.append(A("<b>Types of Relevance Feedback:</b>"))
story.append(B("<b>Explicit feedback:</b> User directly marks results as relevant/not relevant. Accurate but requires user effort."))
story.append(B("<b>Implicit feedback:</b> System infers relevance from user behavior — clicks, time spent, scrolling. No user effort but less accurate."))
story.append(B("<b>Pseudo relevance feedback (blind feedback):</b> System automatically assumes top-k results are relevant and uses them to expand query. No user involvement."))
story.append(A("<b>Rocchio Algorithm (most important for exam):</b>"))
story.append(Paragraph(
    "New Query Vector = alpha × Original_Query\n"
    "                 + beta  × (sum of Relevant Doc Vectors / |Relevant Docs|)\n"
    "                 - gamma × (sum of Non-Relevant Doc Vectors / |Non-Relevant Docs|)", code_style))
story.append(A("Alpha, beta, gamma are weights (typically alpha=1, beta=0.75, gamma=0.15). This moves the query vector closer to relevant docs and away from non-relevant docs."))
story.append(A("<b>Role in improving search:</b>"))
story.append(B("Handles query ambiguity — user clarifies intent through feedback."))
story.append(B("Discovers related terms not in original query."))
story.append(B("Personalizes search results to individual user needs."))
story.append(Ex("User searches 'jaguar'. Gets results about both the car and the animal. Marks car-related pages as relevant. System learns → next query focuses on Jaguar cars."))
story.append(hr())

# ── Q41 ───────────────────────────────────────────────────────────────────────
story.append(Q(41, "Explain query reformulation and its different types."))
story.append(A("Query reformulation is the process of modifying an original search query to improve retrieval performance. It is used when the initial results are not satisfactory."))
story.append(A("<b>Why needed?</b> Users often don't know the exact terms used in relevant documents. They may use synonyms, abbreviations, or vague terms."))
story.append(A("<b>Types of Query Reformulation:</b>"))
story.append(B("<b>1. Query Expansion:</b> Adding new terms to the original query. Subtypes: Thesaurus-based (add synonyms), Relevance feedback-based (add terms from relevant docs), Pseudo-relevance based (automatic top-k assumption)."))
story.append(B("<b>2. Query Reduction:</b> Removing less important terms to focus on the most relevant ones. Useful when query is too long."))
story.append(B("<b>3. Query Substitution:</b> Replacing query terms with better alternatives. Using spelling correction, stemming, or domain-specific vocabulary."))
story.append(B("<b>4. Query Relaxation:</b> Making a strict query less specific. Example: 'hotels in South Mumbai near sea' → relax to 'hotels in Mumbai'. Used when original query returns too few results."))
story.append(B("<b>5. Query Refinement via Spelling Correction:</b> 'Ambani biographi' → corrected to 'Ambani biography'."))
story.append(B("<b>6. Structured Query Reformulation:</b> Adding logical operators or field restrictions. Example: author:Rabindranath title:Gitanjali."))
story.append(B("<b>7. Query Suggestion / Auto-complete:</b> Suggesting alternative queries based on user's partial input and search logs."))
story.append(Ex("Original query: 'heart doctor'. Reformulated: 'cardiologist cardiac doctor heart specialist physician'. Now retrieves medical documents that use formal terminology."))
story.append(hr())

# ── Q42 ───────────────────────────────────────────────────────────────────────
story.append(Q(42, "Explain the Rocchio algorithm and its role in relevance feedback."))
story.append(A("The Rocchio algorithm is the most famous and widely used method for relevance feedback in the Vector Space Model. It modifies the query vector based on user feedback to move it closer to relevant documents and farther from non-relevant ones."))
story.append(A("<b>The Formula:</b>"))
story.append(Paragraph(
    "Q_new = alpha × Q_old\n"
    "       + beta  × (1/|Dr|) × SUM of all relevant document vectors\n"
    "       - gamma × (1/|Dnr|) × SUM of all non-relevant document vectors\n\n"
    "Where:\n"
    "  alpha = weight for original query (typically 1.0)\n"
    "  beta  = weight for relevant docs   (typically 0.75)\n"
    "  gamma = weight for non-relevant docs (typically 0.15)\n"
    "  Dr    = set of relevant documents marked by user\n"
    "  Dnr   = set of non-relevant documents marked by user", code_style))
story.append(A("<b>Intuition:</b>"))
story.append(B("Start with original query vector."))
story.append(B("Move it TOWARDS the centroid of relevant documents (add beta term)."))
story.append(B("Move it AWAY FROM the centroid of non-relevant documents (subtract gamma term)."))
story.append(B("The new query vector now represents a better description of what the user wants."))
story.append(A("<b>Positive Rocchio:</b> If gamma=0, only use positive (relevant) feedback. Safer and often used."))
story.append(A("<b>Limitations:</b>"))
story.append(B("Assumes user feedback is accurate — one wrong judgment can mislead the system."))
story.append(B("Works in VSM only — not directly applicable to language models."))
story.append(B("Long revised queries may be inefficient."))
story.append(Ex("User searches 'python' (wants programming). Marks programming-related results as relevant. Rocchio adds terms like 'programming', 'code', 'language' and moves query away from 'snake', 'animal' terms."))
story.append(hr())

# ── Q43 ───────────────────────────────────────────────────────────────────────
story.append(Q(43, "Explain the basic components of a web search engine and how they work together to retrieve relevant results."))
story.append(A("A web search engine is a complex system with multiple components working together. Here is how each component works:"))
story.append(B("<b>1. Web Crawler (Spider/Bot):</b> Automatically browses the web and downloads web pages. Starts with seed URLs, follows links to discover new pages. Respects robots.txt file. Stores downloaded pages for indexing."))
story.append(B("<b>2. Document Pre-processor:</b> Parses HTML to extract text. Performs tokenization (split into words), stopword removal, stemming/lemmatization. Creates a clean text representation."))
story.append(B("<b>3. Indexer:</b> Builds the inverted index from processed documents. Stores term → document ID, frequency, position mappings. Also computes TF-IDF weights. Compresses and stores the index efficiently."))
story.append(B("<b>4. Query Processor:</b> Receives user's query, processes it (tokenization, stemming). Applies query expansion if needed. Converts query to internal representation."))
story.append(B("<b>5. Ranking Engine:</b> Uses the inverted index to find relevant documents. Applies ranking algorithms — TF-IDF, BM25, PageRank, machine learning models. Returns top-k documents sorted by relevance score."))
story.append(B("<b>6. Results Presenter:</b> Formats top results for display. Shows title, URL, snippet (summary of relevant text). May add features like images, knowledge panels, ads."))
story.append(B("<b>7. Link Analyzer:</b> Computes PageRank and HITS scores. Uses link structure to determine page authority/importance."))
story.append(A("<b>The flow:</b>"))
story.append(Paragraph(
    "Crawler → Downloads pages\n"
    "  ↓\n"
    "Pre-processor → Cleans text\n"
    "  ↓\n"
    "Indexer → Builds inverted index\n"
    "  ↓ (offline, done in advance)\n"
    "Query → Query Processor → Ranking Engine → Top Results → User", code_style))
story.append(hr())

# ── Q44 ───────────────────────────────────────────────────────────────────────
story.append(Q(44, "Compare the Vector Space Model (VSM) and Probabilistic Model in IR."))
data = [
    ["Feature", "Vector Space Model (VSM)", "Probabilistic Model"],
    ["Basic idea", "Documents and queries as vectors in term space", "Estimates probability of relevance"],
    ["Ranking basis", "Cosine similarity between query and doc vectors", "P(Relevant | Document, Query)"],
    ["Term weight", "TF-IDF", "BM25 weights, probability of term occurrence"],
    ["Feedback", "Rocchio algorithm modifies query vector", "Probability estimates updated"],
    ["Key algorithm", "Cosine similarity ranking", "BM25 / Okapi, Language Models"],
    ["Assumption", "Docs are points in vector space", "Docs either relevant or not (binary)"],
    ["Transparency", "Easy to understand and implement", "Mathematically rigorous"],
    ["Handles length?", "Through TF-IDF normalization", "BM25 has explicit length normalization"],
    ["Performance", "Good baseline", "BM25 generally outperforms VSM"],
]
t = Table(data, colWidths=[3.5*cm, 6*cm, 7*cm])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), BLUE),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,-1), 8.5),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT]),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#93c5fd")),
    ('PADDING', (0,0), (-1,-1), 4),
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
]))
story.append(space(4))
story.append(t)
story.append(Tip("Both models are important. VSM is simpler to understand; Probabilistic (BM25) often gives better real-world results."))
story.append(hr())

# ── Q45 ───────────────────────────────────────────────────────────────────────
story.append(Q(45, "Explain the different term weighting schemes used in Information Retrieval and compare their effectiveness."))
story.append(A("Term weighting assigns importance scores to words in documents for retrieval purposes. Different schemes exist:"))
story.append(B("<b>1. Binary weighting:</b> 1 if term present, 0 if absent. Simple but ignores frequency. Poor performance."))
story.append(B("<b>2. Term Frequency (TF):</b> Count of how many times term appears. Gives more weight to frequent terms. Problem: common words like 'the' get high weight unfairly."))
story.append(B("<b>3. TF-IDF:</b> TF × log(N/df). Balances term frequency with rarity across corpus. Most widely used. Rare, frequently-occurring terms in a document get highest weight."))
story.append(B("<b>4. Log-normalized TF:</b> 1 + log(TF) instead of raw TF. Reduces impact of very high-frequency terms. Prevents one word from dominating."))
story.append(B("<b>5. BM25 (Best Match 25):</b> Advanced probabilistic weighting. Accounts for term frequency saturation (adding more occurrences of a term gives diminishing returns) AND document length normalization (penalizes unnecessarily long documents)."))
story.append(Paragraph(
    "BM25_score = IDF × [TF × (k1+1)] / [TF + k1 × (1 - b + b × (dl/avgdl))]\n"
    "  k1 = TF saturation factor (typically 1.2-2.0)\n"
    "  b  = length normalization factor (typically 0.75)\n"
    "  dl = document length, avgdl = average doc length", code_style))
story.append(A("<b>Effectiveness comparison:</b> Binary < TF < TF-IDF < BM25 (in general performance)."))
story.append(Ex("For query 'cricket', document with 'cricket' appearing 10 times gets much higher TF. But with log-TF, diminishing returns apply. BM25 additionally ensures a short 2-page article with 10 'cricket' mentions is NOT unfairly ranked below a 100-page book with 10 mentions."))
story.append(hr())

# ── Q46 ───────────────────────────────────────────────────────────────────────
story.append(Q(46, "Discuss the role of normalization techniques in text classification and retrieval."))
story.append(A("Normalization standardizes text or vectors to remove unimportant variations and make comparisons fair. There are two main types: text normalization and vector normalization."))
story.append(A("<b>Text Normalization Techniques:</b>"))
story.append(B("<b>Case normalization:</b> Convert all text to lowercase. 'Cricket', 'CRICKET', 'cricket' all become 'cricket' → treated as same word."))
story.append(B("<b>Stemming:</b> Reduce words to their root. 'playing', 'played', 'plays' → 'play'. Reduces vocabulary size."))
story.append(B("<b>Lemmatization:</b> Linguistically correct root form. 'better' → 'good'. More accurate than stemming."))
story.append(B("<b>Stopword removal:</b> Remove very common words with little information — 'the', 'is', 'and'."))
story.append(B("<b>Punctuation and special character removal:</b> Remove commas, periods, etc."))
story.append(B("<b>Accent normalization:</b> 'naïve' → 'naive'. Makes matching language-independent."))
story.append(A("<b>Vector Normalization Techniques:</b>"))
story.append(B("<b>L2 normalization (unit vector):</b> Divide each vector by its magnitude → all vectors have length 1. This is what cosine similarity uses implicitly."))
story.append(B("<b>TF normalization:</b> Divide TF by max TF in document to prevent very long documents from dominating."))
story.append(B("<b>Document length normalization (BM25):</b> Adjust scores based on document length to prevent longer documents from always winning."))
story.append(A("<b>Role in classification and retrieval:</b>"))
story.append(B("Makes comparison fair — short and long documents compared on equal terms."))
story.append(B("Reduces vocabulary size — improves speed and reduces sparsity."))
story.append(B("Better generalization — model sees 'run', 'running', 'ran' as same concept."))
story.append(Ex("Without normalization: 'India' and 'india' are different terms, vocabulary doubles unnecessarily. With case normalization, both map to 'india' — better matching."))
story.append(hr())

# ── Q47 ───────────────────────────────────────────────────────────────────────
story.append(Q(47, "Discuss the challenges involved in web crawling and how they are addressed."))
story.append(A("Web crawling is the process of automatically browsing the web to collect pages for indexing. It faces many challenges at web scale (billions of pages)."))
story.append(A("<b>Challenges and Solutions:</b>"))
story.append(B("<b>1. Scale:</b> Billions of web pages exist. Solution: Distributed crawling — thousands of crawlers running in parallel across multiple data centers."))
story.append(B("<b>2. Freshness (keeping content up-to-date):</b> Web pages change frequently. Solution: Crawl popular/frequently-changing pages more often. Use HTTP Last-Modified headers to check if page changed."))
story.append(B("<b>3. Duplicate content:</b> Same content on multiple URLs. Solution: Use URL canonicalization and content hashing (fingerprinting) to detect near-duplicates."))
story.append(B("<b>4. Politeness / Server overload:</b> Crawling too fast can overload web servers. Solution: Implement crawl delays, respect robots.txt file that tells crawlers which pages NOT to crawl."))
story.append(B("<b>5. Trap pages / Spider traps:</b> Infinite loops of dynamically generated pages (e.g., calendar pages generating infinite future dates). Solution: Limit crawl depth, detect repeated patterns in URLs."))
story.append(B("<b>6. Hidden web / Deep web:</b> Content behind login pages, forms, or JavaScript rendering. Solution: Headless browsers (like Puppeteer) to render JavaScript. Login-requiring pages usually not crawled."))
story.append(B("<b>7. Link spam and low-quality pages:</b> Many pages have no useful content. Solution: Prioritize high-PageRank seed URLs. Filter low-quality content."))
story.append(B("<b>8. URL normalization:</b> http://site.com vs https://site.com vs www.site.com are same. Solution: Canonical URL detection."))
story.append(Ex("Googlebot (Google's crawler) uses all these techniques. It has a priority queue of URLs sorted by importance. Fetches millions of pages per second from distributed servers worldwide."))
story.append(hr())

# ── Q48 ───────────────────────────────────────────────────────────────────────
story.append(Q(48, "Explain the concept of language models in IR and how they are used for ranking documents."))
story.append(A("Language models (LM) in IR estimate the probability that a given document 'generated' a particular query. The core idea: if a document is really about the query topic, it should be likely to produce the query words."))
story.append(A("<b>Query Likelihood Model:</b> Rank documents by P(Query | Document) — the probability that the document would generate the query terms."))
story.append(Paragraph(
    "P(Query | Document) = Product of P(each query term | Document)\n"
    "P(term | Document) = TF(term, doc) / Total terms in doc\n\n"
    "For query 'cricket bat':\n"
    "  P('cricket','bat' | D1) = P('cricket'|D1) × P('bat'|D1)", code_style))
story.append(A("<b>Problem — Zero probability:</b> If a query word never appears in a document, P=0, making entire probability zero. This is solved by smoothing."))
story.append(A("<b>Smoothing Techniques:</b>"))
story.append(B("<b>Laplace (add-one) smoothing:</b> Add 1 to every term count. Simple but not very effective for IR."))
story.append(B("<b>Jelinek-Mercer (JM) smoothing:</b> Mix document model with collection (background) model using parameter λ."))
story.append(Paragraph("P_smooth(t|D) = λ × P(t|D) + (1-λ) × P(t|Collection)", code_style))
story.append(B("<b>Dirichlet smoothing:</b> Uses parameter mu (μ) to control smoothing amount based on document length. More smoothing for short documents."))
story.append(A("<b>KL-Divergence Retrieval Model:</b> Instead of query likelihood, minimize the KL-divergence (difference) between query language model and document language model. More similar models → lower KL-divergence → higher relevance."))
story.append(Ex("Document D1 mentions 'cricket' 10 times out of 100 words → P('cricket'|D1) = 0.1. Query is 'cricket'. D1 gets high score. A document never mentioning cricket gets P=0 before smoothing."))
story.append(hr())

# ── Q49 ───────────────────────────────────────────────────────────────────────
story.append(Q(49, "Explain the working of the Naive Bayes classifier for text classification with an example."))
story.append(A("Naive Bayes is a probabilistic classifier based on Bayes' Theorem with the 'naive' assumption that all features (words) are independent of each other given the class."))
story.append(A("<b>Bayes' Theorem applied to text:</b>"))
story.append(Paragraph(
    "P(Class | Document) ∝ P(Class) × P(Document | Class)\n"
    "P(Document | Class) = P(w1|Class) × P(w2|Class) × ... × P(wn|Class)  [Naive assumption]", code_style))
story.append(A("<b>Step-by-Step Example — Spam Detection:</b>"))
story.append(A("<b>Training Data:</b>"))
story.append(Paragraph(
    "SPAM:    'win lottery prize', 'free money now', 'lottery winner prize'\n"
    "NOT SPAM: 'meeting tomorrow', 'project deadline', 'submit report'", code_style))
story.append(A("<b>Step 1: Calculate Prior Probabilities</b>"))
story.append(Paragraph(
    "P(Spam)    = 3/6 = 0.5\n"
    "P(Not Spam) = 3/6 = 0.5", code_style))
story.append(A("<b>Step 2: Calculate Word Probabilities</b>"))
story.append(Paragraph(
    "In Spam class, total words = 9\n"
    "P('lottery'|Spam) = 2/9 ≈ 0.22  [appears twice in spam]\n"
    "P('prize'|Spam)   = 2/9 ≈ 0.22\n"
    "P('lottery'|Not Spam) = 0/9 → with Laplace smoothing = 1/12 ≈ 0.08", code_style))
story.append(A("<b>Step 3: Classify new email: 'win lottery prize'</b>"))
story.append(Paragraph(
    "P(Spam | email) ∝ 0.5 × P('win'|Spam) × P('lottery'|Spam) × P('prize'|Spam)\n"
    "                ∝ 0.5 × 0.11 × 0.22 × 0.22 = 0.00266\n\n"
    "P(Not Spam | email) ∝ 0.5 × P('win'|Not Spam) × P('lottery'|Not Spam) × P('prize'|Not Spam)\n"
    "                    ∝ 0.5 × 0.08 × 0.08 × 0.08 = 0.000256\n\n"
    "0.00266 > 0.000256 → CLASSIFIED AS SPAM ✓", code_style))
story.append(A("<b>Important Notes:</b>"))
story.append(B("Use log probabilities in practice to avoid underflow (very small numbers)."))
story.append(B("Always use Laplace smoothing (add 1) to avoid zero probabilities for unseen words."))
story.append(B("Despite the naive assumption, Naive Bayes performs surprisingly well for text."))
story.append(Tip("Log P(spam|doc) = log P(spam) + sum of log P(word|spam) for each word. This is computationally stable."))
story.append(hr())

# ── Q50 ───────────────────────────────────────────────────────────────────────
story.append(Q(50, "Discuss the importance of feature extraction in text mining and explain common techniques used."))
story.append(A("Feature extraction converts raw text into a numerical form (features) that machine learning algorithms can process. It is one of the most critical steps in any text mining pipeline."))
story.append(A("<b>Why Feature Extraction is Important:</b>"))
story.append(B("Computers cannot process raw text directly — they need numbers."))
story.append(B("Good features → good model performance. Bad features → even the best algorithm fails."))
story.append(B("Reduces dimensionality while preserving important information."))
story.append(B("Captures the semantic meaning or statistical patterns of text."))
story.append(A("<b>Common Feature Extraction Techniques:</b>"))
story.append(B("<b>1. Bag of Words (BoW):</b> Represent document as a vector of word counts. Simple and effective. Ignores word order and grammar."))
story.append(Paragraph(
    "Doc: 'I love cricket and cricket is great'\n"
    "BoW: {I:1, love:1, cricket:2, and:1, is:1, great:1}", code_style))
story.append(B("<b>2. TF-IDF Vectors:</b> Improvement over BoW — weights terms by importance. Rare, document-specific terms get higher weights."))
story.append(B("<b>3. N-grams:</b> Instead of single words, capture sequences of n words. Bigrams: 'machine learning', 'text mining'. Captures some context that BoW misses."))
story.append(B("<b>4. Word Embeddings (Word2Vec, GloVe, FastText):</b> Map each word to a dense vector (e.g., 300 dimensions) trained on large corpora. Captures semantic similarity — 'king' - 'man' + 'woman' ≈ 'queen'."))
story.append(B("<b>5. Document Embeddings (Doc2Vec, BERT):</b> Extend word embeddings to entire documents. BERT uses transformer architecture to capture deep context."))
story.append(B("<b>6. Character-level features:</b> Extract features based on characters, subwords. Handles typos and morphologically rich languages."))
story.append(B("<b>7. POS tags and syntactic features:</b> Part-of-speech tags (noun, verb, adjective) as features for complex NLP tasks."))
story.append(B("<b>8. Named Entity features:</b> Presence of person names, locations, organizations. Useful for news categorization."))
story.append(Ex("For sentiment analysis, TF-IDF extracts words like 'excellent', 'terrible', 'amazing' as important features. Word2Vec additionally knows 'excellent' and 'great' are similar even if both don't appear in training data together."))
story.append(Tip("Modern NLP uses BERT/Transformer-based features which understand context — 'bank' in 'river bank' vs 'bank account' get different representations."))

# Final page
story.append(PageBreak())
story.append(space(20))
story.append(Paragraph("All The Best for Your Exam!", title_style))
story.append(space(10))
story.append(Paragraph("Quick Revision Tips", 
    ParagraphStyle("rev", parent=subtitle_style, fontSize=14, textColor=DARKBLUE)))
story.append(space(8))
tips = [
    ("3-mark questions", "Write 3-4 points + 1 example. Keep it short and clear. ~150 words."),
    ("5-mark questions", "Write intro + 5-6 detailed points + example + conclusion. ~300-400 words."),
    ("Must-know formulas", "TF-IDF, Cosine Similarity, Rocchio Algorithm, PageRank, BM25, Bayes Theorem"),
    ("Key algorithms", "k-Means, DBSCAN, Naive Bayes, Rocchio, PageRank, HITS"),
    ("Most important topics", "Inverted Index, TF-IDF, VSM, PageRank, Naive Bayes, k-Means, Relevance Feedback"),
    ("Time management", "Attempt all questions. If you don't know fully — write what you know + example."),
]
for tip in tips:
    story.append(Paragraph(f"<b>{tip[0]}:</b> {tip[1]}", 
        ParagraphStyle("rtip", parent=ans_style, spaceBefore=6, backColor=LIGHTGRN, 
                       borderPad=5, leading=16)))
story.append(space(20))
story.append(Paragraph("Remember: Understanding is better than memorizing. Read each answer once with full attention, understand the logic, then you can write it in your own words!",
    ParagraphStyle("final", parent=ans_style, fontSize=11, textColor=DARKBLUE, 
                   alignment=TA_CENTER, fontName="Helvetica-Bold")))

# ─── Build ────────────────────────────────────────────────────────────────────
doc.build(story)
print("PDF created successfully!")
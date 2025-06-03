DROP TABLE IF EXISTS testimonials;
DROP TABLE IF EXISTS contacts;
DROP TABLE IF EXISTS utm_links;

CREATE TABLE testimonials (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  text TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE contacts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  phone TEXT NOT NULL,
  issue TEXT NOT NULL,
  message TEXT NOT NULL,
  source TEXT,
  utm_source TEXT,
  utm_medium TEXT,
  utm_campaign TEXT,
  utm_term TEXT,
  utm_content TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE utm_links (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  base_url TEXT NOT NULL,
  utm_source TEXT NOT NULL,
  utm_medium TEXT NOT NULL,
  utm_campaign TEXT NOT NULL,
  utm_term TEXT,
  utm_content TEXT,
  short_description TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  last_updated TIMESTAMP
);

-- Dados iniciais para depoimentos
INSERT INTO testimonials (name, text)
VALUES 
  ('Maria Silva', 'Depois de dois anos sofrendo com dor lombar, finalmente encontrei um treinamento que me ajudou a voltar a ter qualidade de vida. Muito obrigada!'),
  ('Juliana Mendes', 'A metodologia da Consultoria Calazans é incrível! Consegui recuperar meu corpo após a gravidez de uma forma segura e eficiente.'),
  ('Fernanda Oliveira', 'Tinha desistido de me exercitar por causa da minha hérnia de disco, mas os treinos personalizados mudaram minha vida. Recomendo demais!');

-- Dados iniciais para links UTM
INSERT INTO utm_links (name, base_url, utm_source, utm_medium, utm_campaign, utm_term, utm_content, short_description)
VALUES
  ('Campanha Instagram Julho', 'https://consultoriacalazans.com', 'instagram', 'social', 'julho2023', 'recuperacao', 'post1', 'Campanha para divulgação no Instagram durante julho'),
  ('Google Ads - Hérnia', 'https://consultoriacalazans.com', 'google', 'cpc', 'hernia2023', 'dor lombar', 'anuncio1', 'Campanha no Google Ads focada em hérnia de disco'); 
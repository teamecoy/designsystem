/* Lower home-page sections: range bands, bundle tabs, stats, founders, impact. */
const { Button, FilterPill, ProductCard, Badge } = window.EcoyDesignSystem_9bc9f5;

/* A range band: full-bleed shallow banner with an eyebrow + big title, then a product row and one text CTA. */
function RangeBand({ eyebrow, flag, title, blurb, image, cta, products, onOpen }) {
  return (
    <section style={{ paddingBottom: 72 }}>
      <div style={{ position: 'relative', aspectRatio: '3.8 / 1', minHeight: 260, overflow: 'hidden' }}>
        <img src={EIMG + image} alt="" style={{ width: '100%', height: '100%', objectFit: 'cover', objectPosition: 'center 45%' }} />
        <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(90deg, rgba(28,28,28,.4) 0%, rgba(28,28,28,.1) 50%, rgba(28,28,28,0) 75%)' }} />
        {flag ? (
          <div style={{ position: 'absolute', top: 20, left: 24 }}><Badge category="value">{flag}</Badge></div>
        ) : null}
        <div style={{ position: 'absolute', left: 0, right: 0, bottom: '10%' }}>
          <div style={{ maxWidth: 'var(--container-max)', margin: '0 auto', padding: '0 24px', color: 'var(--color-off-white)' }}>
            <div className="font-text" style={{ fontSize: 12, fontWeight: 500, letterSpacing: '.12em', marginBottom: 8 }}>{eyebrow}</div>
            <h2 style={{ color: 'var(--color-off-white)', fontSize: 56, fontWeight: 400, lineHeight: 1.04, letterSpacing: '-0.03em', margin: '0 0 10px' }}>{title}</h2>
            <p className="font-text" style={{ fontSize: 16, margin: 0 }}>{blurb}</p>
          </div>
        </div>
      </div>
      <div style={{ maxWidth: 'var(--container-max)', margin: '0 auto', padding: '40px 24px 0' }}>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, minmax(0, 1fr))', gap: 24 }}>
          {products.slice(0, 4).map(p => <ProductCard key={p.id} {...cardProps(p)} onClick={() => onOpen(p)} />)}
        </div>
        <div style={{ marginTop: 28 }}>
          <a href="#" onClick={e => { e.preventDefault(); onOpen(products[0]); }} className="font-text"
            style={{ fontSize: 15, color: 'var(--color-deep-green)', textDecoration: 'underline', textUnderlineOffset: 5 }}>{cta}</a>
        </div>
      </div>
    </section>
  );
}

const BUNDLES = {
  'Bamboo bundles': [
    { id: 'b1', name: 'Bamboo Winter Warmer Bundle', img: 'tile-5921a53762-a.jpg', wasPrice: '$399', price: '$339', from: true, discount: '15% off' },
    { id: 'b2', name: 'All Seasons Doona Bundle', img: 'tile-dddf8fb0fd-a.jpg', wasPrice: '$613', price: '$490', from: true, discount: '20% off' },
    { id: 'b3', name: 'Bamboo Ultimate Bedding Bundle', img: 'tile-de3ec98616-a.jpg', wasPrice: '$1,041', price: '$781', from: true, discount: '25% off' },
    { id: 'b4', name: 'Bamboo Ultimate No Top Sheet Bundle', img: 'tile-12c712b3b1-b.jpg', wasPrice: '$1,021', price: '$766', from: true, discount: '25% off' }
  ],
  'Flannelette bundles': [
    { id: 'f1', name: 'Flannelette Winter Warmer Bundle', img: 'tile-52bb475893-b.jpg', wasPrice: '$286', price: '$229', from: true, discount: '20% off' },
    { id: 'f2', name: 'Flannelette All Seasons Bundle', img: 'tile-de3ec98616-a.jpg', wasPrice: '$500', price: '$400', from: true, discount: '20% off' },
    { id: 'f3', name: 'Flannelette Ultimate Bedding Bundle', img: 'tile-52bb475893-b.jpg', wasPrice: '$835', price: '$668', from: true, discount: '20% off' },
    { id: 'f4', name: 'Flannelette Ultimate No Top Sheet Bundle', img: 'tile-dddf8fb0fd-a.jpg', wasPrice: '$813', price: '$650', from: true, discount: '20% off' }
  ],
  'Corduroy bundles': [
    { id: 'c1', name: 'Corduroy Winter Warmer Bundle', img: 'tile-75fbe91a96-b.jpg', wasPrice: '$409', price: '$348', from: true, discount: '15% off' },
    { id: 'c2', name: 'Corduroy All Seasons Bundle', img: 'tile-e93e6ca2fb-a.jpg', wasPrice: '$623', price: '$498', from: true, discount: '20% off' }
  ]
};

function BundleTabs({ onOpen }) {
  const tabs = Object.keys(BUNDLES);
  const [tab, setTab] = React.useState(tabs[0]);
  return (
    <section style={{ maxWidth: 'var(--container-max)', margin: '0 auto', padding: '0 24px 80px' }}>
      <h2 style={{ fontSize: 36, marginBottom: 24 }}>Save 30% on Quilt Bundles</h2>
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8, marginBottom: 32 }}>
        {tabs.map(t => <FilterPill key={t} active={tab === t} onClick={() => setTab(t)}>{t}</FilterPill>)}
      </div>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, minmax(0, 1fr))', gap: 24 }}>
        {BUNDLES[tab].map(p => <ProductCard key={p.id} {...cardProps(p)} onClick={() => onOpen(p)} />)}
      </div>
    </section>
  );
}

/* Proof band: deep green, centred heading, three thin-line icons over big percentages. */
const STATS = [
  { icon: 'heart', value: '95.60%', copy: 'of customers rate Ecoy a 4 or 5-star sleep experience' },
  { icon: 'flower', value: '90.51%', copy: 'confirmed their sleep quality improved after switching to Ecoy' },
  { icon: 'lock', value: '63.31%', copy: 'of Ecoy buyers upgraded from traditional Cotton sheets' }
];

function StatsBand() {
  return (
    <section style={{ background: 'var(--color-deep-green)', color: 'var(--color-off-white)', padding: '72px 24px' }}>
      <div style={{ maxWidth: 'var(--container-max)', margin: '0 auto' }}>
        <h2 style={{ color: 'var(--color-off-white)', fontSize: 36, fontWeight: 400, textAlign: 'center', margin: '0 0 56px' }}>Proven benefits, proven results</h2>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, minmax(0, 1fr))', gap: 48 }}>
          {STATS.map(s => (
            <div key={s.value}>
              <Icon name={s.icon} size={40} weight={1.4} color="var(--color-off-white)" />
              <div style={{ fontFamily: 'var(--font-display)', fontSize: 40, fontWeight: 400, letterSpacing: '-0.02em', margin: '20px 0 14px' }}>{s.value}</div>
              <p className="font-text" style={{ fontSize: 15, lineHeight: 1.5, color: 'var(--color-off-white)', maxWidth: 320, margin: 0 }}>{s.copy}</p>
            </div>
          ))}
        </div>
        <p className="font-text" style={{ fontSize: 13, color: 'var(--color-light-green)', textAlign: 'center', margin: '48px 0 0' }}>4,500+ Reviews · Loved by 70,000+ Aussies &amp; Kiwis</p>
      </div>
    </section>
  );
}

function Founders() {
  return (
    <section style={{ maxWidth: 'var(--container-max)', margin: '0 auto', padding: '80px 24px', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 56, alignItems: 'center' }}>
      <img src={CDN + 'About_us_Founders.jpg?v=1779373762&width=1000'} alt="Sam and James, founders of Ecoy"
        style={{ width: '100%', aspectRatio: '4/3', objectFit: 'cover', borderRadius: 'var(--radius-card)' }} />
      <div>
        <h2 style={{ fontSize: 32, marginBottom: 18 }}>From the founders</h2>
        <p className="font-text text-body-legible" style={{ maxWidth: 460 }}>Ecoy was founded in Brissie by two best mates, Sam and James, on a mission to solve their problem of sweaty, sleepless nights as two hot sleepers.</p>
        <p className="font-text text-body-legible" style={{ maxWidth: 460 }}>As Aussies who love quality sleep, they found bamboo — a sustainable, fast-growing fabric that’s naturally cooling and luxuriously soft.</p>
        <p className="font-text text-body-legible" style={{ maxWidth: 460 }}>Proudly Aussie owned and operated, Ecoy is all about helping hot sleepers get a better night’s sleep with cooling bedding designed for an increasingly hot climate.</p>
        <p className="font-text" style={{ fontWeight: 600, marginBottom: 20 }}>Sam &amp; James, Founders of Ecoy</p>
        <a href="#" onClick={e => e.preventDefault()} className="font-text" style={{ fontSize: 15, color: 'var(--color-deep-green)', textDecoration: 'underline', textUnderlineOffset: 5 }}>Our story</a>
      </div>
    </section>
  );
}

function ImpactBand() {
  const items = [
    { img: 'OEKO_TEX_STANDARD_100-2022.png?v=1779538177&width=400', h: 'Product Tested', copy: 'STANDARD 100 by OEKO-TEX® is one of the world’s best-known labels for textiles tested for harmful substances.' },
    { img: 'image_7.jpg?v=1779111842&width=600', h: '$1 donated on every sale', copy: 'Ecoy supports domestic and abroad NGO projects related to environmental and human welfare with i=Change.' }
  ];
  return (
    <section style={{ maxWidth: 'var(--container-max)', margin: '0 auto', padding: '0 24px 88px' }}>
      <h2 style={{ fontSize: 32, marginBottom: 32 }}>Driving measurable impact with our community</h2>
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 24 }}>
        {items.map(i => (
          <div key={i.h} style={{ display: 'flex', gap: 20, alignItems: 'flex-start' }}>
            <img src={CDN + i.img} alt="" style={{ width: 96, height: 96, objectFit: 'contain', flex: 'none' }} />
            <div>
              <h3 style={{ marginBottom: 8 }}>{i.h}</h3>
              <p className="font-text text-body-legible" style={{ fontSize: 15, margin: 0 }}>{i.copy}</p>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}

Object.assign(window, { RangeBand, BundleTabs, StatsBand, Founders, ImpactBand, BUNDLES, STATS });

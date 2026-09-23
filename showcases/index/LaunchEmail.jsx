/*
 * STATUS (2026-09-23): reconciled from the Ecoy Design System Claude Design
 * artifact into this repo (was built there and never pushed back — see
 * showcases/README.md). Runs only inside that artifact today: it needs
 * `window.EcoyDesignSystem_9bc9f5` (the artifact's compiled component
 * bundle — Button/Logo/Eyebrow/ColourBlock/FeatureChip/Badge/PillarShape/
 * ReviewPillar/Ticker/HandDrawn) and the sibling Shell.jsx it's normally
 * loaded alongside, neither of which exist in this repo yet. Do not treat
 * this as runnable in isolation until that bundle is exported here too.
 */
const { Button, Logo, Eyebrow, ColourBlock, FeatureChip, Badge, PillarShape, ReviewPillar, Ticker, HandDrawn } = window.EcoyDesignSystem_9bc9f5;
const B = '../../';
const IMG = B + 'assets/imagery/';

const edmType = {
  h1: { fontFamily: 'var(--font-display)', fontWeight: 700, fontSize: 40, lineHeight: 1.2, letterSpacing: '-0.02em', margin: 0 },
  h2: { fontFamily: 'var(--font-display)', fontWeight: 700, fontSize: 28, lineHeight: 1.2, letterSpacing: '-0.02em', margin: 0 },
  body: { fontFamily: 'var(--font-text)', fontSize: 15, lineHeight: 1.4, letterSpacing: '-0.02em', margin: 0 },
  small: { fontFamily: 'var(--font-text)', fontSize: 12, lineHeight: 1.4, letterSpacing: '-0.02em', margin: 0 }
};

function Hero() {
  return (
    <div style={{ position: 'relative', height: 620, overflow: 'hidden' }}>
      <img src={IMG + 'tile-e93e6ca2fb-a.jpg'} alt="" style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
      <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(180deg, rgba(28,28,28,.28) 0%, rgba(28,28,28,0) 34%, rgba(28,28,28,.55) 100%)' }} />
      <div style={{ position: 'absolute', top: 24, left: 0, right: 0, display: 'grid', placeItems: 'center' }}>
        <Logo variant="white" height={26} basePath={B} />
      </div>
      <div style={{ position: 'absolute', left: 32, right: 32, bottom: 32, color: 'var(--color-off-white)' }}>
        <Eyebrow style={{ color: 'var(--color-off-white)', fontWeight: 600, letterSpacing: '.08em' }}>NEW</Eyebrow>
        <h1 style={{ ...edmType.h1, color: 'var(--color-off-white)', marginBottom: 20 }}>Winter<br />Flannelette</h1>
        <Button variant="light" href="#">Shop the drop</Button>
      </div>
    </div>
  );
}

function BenefitsBlob() {
  return (
    <div style={{ background: 'var(--color-off-white)', padding: '40px 32px', textAlign: 'center' }}>
      <h2 style={{ ...edmType.h2, color: 'var(--color-deep-green)', marginBottom: 6 }}>Warmth without the overheat</h2>
      <p style={{ ...edmType.body, color: 'var(--color-burgundy)', marginBottom: 24 }}>The perfect winter refresh</p>
      <div style={{ position: 'relative', display: 'grid', placeItems: 'center', marginBottom: 24 }}>
        <PillarShape shape="pillar-clover" pillar="climate" size={300} basePath={B} style={{ opacity: .9 }} />
        <img src={IMG + 'tile-52bb475893-b.jpg'} alt="" style={{ position: 'absolute', width: 200, height: 200, objectFit: 'cover', borderRadius: 16 }} />
      </div>
      <div style={{ display: 'flex', flexDirection: 'column', gap: 10, alignItems: 'center' }}>
        <FeatureChip tone="solid">Breathable comfort</FeatureChip>
        <FeatureChip tone="solid">Soft, cosy feel</FeatureChip>
        <FeatureChip tone="solid">5 unique colours</FeatureChip>
      </div>
    </div>
  );
}

/*
 * Real Flannelette Sheet Set photography, resolved from the Shopify Files CDN
 * (assets/resolveImage.js + assets/cdn-catalog.json) rather than pasted from
 * opaque Claude Design upload hashes. This is the actual live 5-colour
 * Flannelette range (assets/colour-status.json) — there is no sixth
 * colourway ("Oat Milk" was never a real Ecoy colourway; it has been
 * removed so the grid matches its own "Five colours" heading).
 */
const COLOURWAYS = [
  { url: 'https://cdn.shopify.com/s/files/1/0498/6100/1367/files/FlannelSheetSet-Solid-Oatmeal-High45-NoTalent-Real-01.webp', name: 'Oatmeal' },
  { url: 'https://cdn.shopify.com/s/files/1/0498/6100/1367/files/FlannelSheetSet-Solid-ForestGreen-High45-NoTalent-Real-01.webp', name: 'Forest' },
  { url: 'https://cdn.shopify.com/s/files/1/0498/6100/1367/files/FlannelSheetSet-Solid-Jacaranda-High45-NoTalent-Real-01.webp', name: 'Jacaranda' },
  { url: 'https://cdn.shopify.com/s/files/1/0498/6100/1367/files/FlannelSheetSet-Solid-Eggplant-High45-NoTalent-Real-01.webp', name: 'Eggplant' },
  { url: 'https://cdn.shopify.com/s/files/1/0498/6100/1367/files/FlannelSheetSet-Solid-Sage-High45-NoTalent-Real-01.webp', name: 'Sage' }
];

function ColourwayGrid() {
  return (
    <ColourBlock ground="light-green" padding="40px 32px">
      <h2 style={{ ...edmType.h2, color: 'var(--color-deep-green)', textAlign: 'center', marginBottom: 20 }}>Five colours. One feeling.</h2>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 12 }}>
        {COLOURWAYS.map(c => (
          <div key={c.name} style={{ position: 'relative', borderRadius: 12, overflow: 'hidden', aspectRatio: '1' }}>
            <img src={c.url} alt={c.name} style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
            <span style={{ position: 'absolute', left: 8, bottom: 8, fontFamily: 'var(--font-display)', fontWeight: 600, fontSize: 14, letterSpacing: '-0.02em', color: 'var(--color-off-white)', textShadow: '0 1px 6px rgba(28,28,28,.5)' }}>{c.name}</span>
          </div>
        ))}
      </div>
      <div style={{ textAlign: 'center', marginTop: 24 }}><Button href="#">Shop sheet sets</Button></div>
    </ColourBlock>
  );
}

function ReviewBand() {
  return (
    <ColourBlock ground="deep-green" padding="40px 32px">
      <div style={{ display: 'grid', placeItems: 'center', marginBottom: 20 }}>
        <ReviewPillar quote="Coolest sheets I've ever slept in. Two winters in and they still feel new." author="Steph M. · Verified buyer" color="var(--color-light-green)" ink="var(--color-deep-green)" size={300} basePath={B} />
      </div>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 8 }}>
        {['tile-75fbe91a96-a.jpg', 'tile-dddf8fb0fd-a.jpg', 'tile-12c712b3b1-a.jpg', 'tile-2a6cb18122-b.jpg'].map(i => (
          <img key={i} src={IMG + i} alt="" style={{ width: '100%', aspectRatio: '1', objectFit: 'cover', borderRadius: 8 }} />
        ))}
      </div>
      <p style={{ ...edmType.small, color: 'var(--color-light-green)', textAlign: 'center', marginTop: 14 }}>Over 40,000 Australians sleeping better · 4.8 average from 6,200 reviews</p>
    </ColourBlock>
  );
}

function CategorySplit() {
  const tiles = [
    { img: 'tile-dddf8fb0fd-b.jpg', label: 'Shop sheets' },
    { img: 'tile-de3ec98616-a.jpg', label: 'Shop quilt covers' }
  ];
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr' }}>
      {tiles.map(t => (
        <div key={t.label} style={{ position: 'relative', aspectRatio: '1' }}>
          <img src={IMG + t.img} alt="" style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
          <div style={{ position: 'absolute', inset: 0, background: 'rgba(0,76,57,.42)', display: 'grid', placeItems: 'center' }}>
            <span style={{ fontFamily: 'var(--font-display)', fontWeight: 700, fontSize: 22, letterSpacing: '-0.02em', color: 'var(--color-off-white)' }}>{t.label}</span>
          </div>
        </div>
      ))}
    </div>
  );
}

function Footer() {
  return (
    <ColourBlock ground="charcoal" padding="36px 32px">
      <div style={{ display: 'grid', placeItems: 'center', gap: 16 }}>
        <Logo variant="white" height={22} basePath={B} />
        <div style={{ display: 'flex', gap: 14, alignItems: 'center' }}>
          <img src={IMG + '3f72ed395a.jpg'} alt="Facebook" style={{ width: 26, height: 26, objectFit: 'contain', mixBlendMode: 'screen' }} />
          <img src={IMG + 'f02166880a.jpg'} alt="Instagram" style={{ width: 26, height: 26, objectFit: 'contain', mixBlendMode: 'screen' }} />
          <img src={IMG + 'd642301560.jpg'} alt="TikTok" style={{ width: 26, height: 26, objectFit: 'contain', mixBlendMode: 'screen' }} />
        </div>
        <p style={{ ...edmType.small, color: 'var(--color-off-white)', opacity: .7, textAlign: 'center', maxWidth: 380 }}>
          You're receiving this because you shopped with Ecoy or signed up for better sleep.<br />Unsubscribe · Update preferences · Ecoy, Sydney NSW
        </p>
      </div>
    </ColourBlock>
  );
}

function LaunchEmail() {
  return (
    <div className="email">
      <Ticker tone="orange" message="Free shipping on orders over $99" />
      <Hero />
      <BenefitsBlob />
      <ColourwayGrid />
      <ReviewBand />
      <CategorySplit />
      <Footer />
    </div>
  );
}

Object.assign(window, { LaunchEmail, Hero, BenefitsBlob, ColourwayGrid, ReviewBand, CategorySplit, Footer });

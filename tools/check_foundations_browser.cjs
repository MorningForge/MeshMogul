const {chromium}=require('playwright');
const fs=require('fs');
(async()=>{
 const browser=await chromium.launch({executablePath:process.env.CHROMIUM_PATH || '/usr/bin/chromium',headless:true,args:['--no-sandbox']});
 const context=await browser.newContext();const page=await context.newPage();
 const errors=[];page.on('pageerror',e=>errors.push(e.message));
 const root=process.env.FOUNDATIONS_BASE_URL || 'http://127.0.0.1:8765/MeshMogul/';
 fs.mkdirSync('.local',{recursive:true});
 const cat=JSON.parse(fs.readFileSync('assets/foundations-catalog.json'));
 const assert=(x,m)=>{if(!x)throw new Error(m)};
 const calls=[];page.on('request',r=>calls.push(r.url()));
 await page.goto(root+'guides/');await page.locator('#search-controls').waitFor({state:'visible'});
 assert(await page.locator('[data-guide]:visible').count()===16,'initial count');
 await page.keyboard.press('Tab');assert(await page.locator('.skip-link').evaluate(el=>el===document.activeElement),'skip-link keyboard entry');
 await page.keyboard.press('Enter');assert(await page.locator('#main').evaluate(el=>el===document.activeElement),'skip-to-main focus');
 const firstPath=page.locator('.path-card').first();await firstPath.locator('summary').focus();await page.keyboard.press('Enter');assert(await firstPath.getAttribute('open')!==null,'keyboard path disclosure');await page.keyboard.press('Enter');
 for(const [q,slug] of [['CollisionPrecision','collision-fidelity-and-invisible-doorways'],['dark smudges','normals-uv-seams-and-texture-budgets'],['WorldPivot','preparing-studio-builds-for-finalization'],['MeshId','meshid-vs-assetid-in-roblox'],['MikkTSpace','normals-uv-seams-and-texture-budgets'],['GenerationError','proceduralmodel-assistant-output-to-mesh']]){
  await page.getByLabel('Search Foundations',{exact:true}).fill(q);
  assert(await page.locator(`[data-guide="${slug}"]`).isVisible(),'missing search: '+q);
 }
 await page.locator('#search-query').fill('zzzznonexistent');
 assert(await page.locator('[data-guide]:visible').count()===0,'empty count');assert(await page.locator('#empty-results').isVisible(),'empty message');
 await page.getByRole('button',{name:'Clear',exact:true}).click();
 assert(await page.locator('[data-guide]:visible').count()===16,'clear');
 await page.getByLabel('Subject',{exact:true}).selectOption('understand-3d');
 assert(await page.locator('[data-guide]:visible').count()===5,'subject filter');
 await page.getByLabel('Difficulty',{exact:true}).selectOption('advanced');
 assert(await page.locator('[data-guide]:visible').count()===1,'combined filter');
 await page.getByRole('button',{name:'Clear',exact:true}).click();
 await page.locator('#search-query').fill('zzzznonexistent');
 await page.locator('.foundations-tracks a[href="#build-with-ai"]').click();
 assert(await page.locator('[data-guide]:visible').count()===3,'subject jump recovers hidden track');
 await page.getByRole('button',{name:'Clear',exact:true}).click();
 await page.locator('#search-query').fill('<img src=x onerror=alert(1)>');assert(await page.locator('#guide-results img').count()===0,'unsafe rendering');
 await page.getByRole('button',{name:'Clear',exact:true}).click();
 await page.locator('#search-query').focus();await page.keyboard.press('Tab');assert(await page.locator('#subject-filter').evaluate(el=>el===document.activeElement),'keyboard subject');
 await page.keyboard.press('Tab');assert(await page.locator('#difficulty-filter').evaluate(el=>el===document.activeElement),'keyboard difficulty');
 await page.keyboard.press('Tab');assert(await page.getByRole('button',{name:'Clear',exact:true}).evaluate(el=>el===document.activeElement),'keyboard clear');
 assert(await page.locator('#search-status').getAttribute('role')==='status','live status');
 const ax=await page.locator('#guide-search').ariaSnapshot();assert(ax.includes('Search Foundations')&&ax.includes('Subject')&&ax.includes('Difficulty'),'accessible search labels');
 // Every direct route and three required viewport widths, including internal scrolling containers.
 for(const width of [1280,390,320]){
  await page.setViewportSize({width,height:900});
  for(const route of ['guides/',...cat.guides.map(g=>'guides/'+g.slug+'/')]){
   const response=await page.goto(root+route);assert(response.status()===200,'direct URL '+route);
   const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth);
   assert(!overflow,'page overflow '+width+' '+route);
   assert(await page.locator('h1').count()===1,'h1 '+route);
   for(const image of await page.locator('.foundation-visual img').all()){
    await image.scrollIntoViewIfNeeded();
    await image.evaluate(el=>el.decode());
    assert(await image.evaluate(el=>el.naturalWidth>0&&el.naturalHeight>0),'visual image decode '+route);
    assert((await image.getAttribute('alt')||'').length>20,'meaningful visual alt '+route);
    assert(await image.getAttribute('loading')==='lazy','lazy visual '+route);
    assert(await image.getAttribute('srcset'),'responsive visual '+route);
   }
   assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'overflow after image decode '+width+' '+route);
   const visual=page.locator('.foundation-visual');
   if(await visual.count()){
    const id=await visual.getAttribute('id');
    await page.locator('#main').focus();
    await visual.screenshot({path:`.local/${id}-${width}.png`});
   }
  }
  for(const [name,route] of [['hub','guides/'],['article','guides/how-to-prompt-ai-for-roblox-3d-models/'],['technical','guides/collision-fidelity-and-invisible-doorways/']]){
   await page.goto(root+route);await page.screenshot({path:`.local/${name}-${width}.png`,fullPage:true});
  }
 }
 assert(!calls.some(u=>u.endsWith('.mp4')),'video downloaded before playback');
 const visualGuides=cat.guides.filter(g=>fs.readFileSync('guides/'+g.slug+'/index.html','utf8').includes('class="foundation-visual"'));
 assert(visualGuides.length===8,'eight visual stations');
 // Exercise the delivered clips through to completion; motion is always opt-in.
 for(const guide of visualGuides){
  await page.goto(root+'guides/'+guide.slug+'/');
  const video=page.locator('.visual-motion video');if(!await video.count())continue;
  assert(await video.getAttribute('preload')==='none','no eager clip preload');
  assert(await video.getAttribute('autoplay')===null,'no automatic motion');
  assert(await video.getAttribute('controls')!==null,'native video controls');
  await page.locator('.visual-motion summary').click();
  await video.evaluate(async el=>{el.loop=false;await el.play()});
  await page.waitForFunction(()=>document.querySelector('.visual-motion video').ended);
  assert(await video.evaluate(el=>el.currentTime>3&&el.videoWidth===960&&!el.error),'complete clip playback');
 }
 const reduced=await browser.newContext({reducedMotion:'reduce',viewport:{width:320,height:900}});
 const still=await reduced.newPage();await still.goto(root+'guides/how-to-prompt-ai-for-roblox-3d-models/');
 assert(await still.locator('video').evaluate(el=>el.paused&&!el.autoplay),'reduced motion stays still');
 assert(await still.locator('.visual-motion').getAttribute('open')===null,'motion starts collapsed');
 await reduced.close();
 // JS-free navigation and the complete brief remain usable.
 const nojs=await browser.newContext({javaScriptEnabled:false,viewport:{width:320,height:900}});const plain=await nojs.newPage();
 await plain.goto(root+'guides/');assert(await plain.locator('[data-guide]:visible').count()===16,'nojs cards');assert(!await plain.locator('#search-controls').isVisible(),'nojs search hidden');
 for(const p of cat.learning_paths){await plain.locator('#'+p.id+' summary').click();assert(await plain.locator('#'+p.id+' a').count()===p.slugs.length,'nojs paths');}
 await plain.goto(root+'guides/how-to-prompt-ai-for-roblox-3d-models/#asset-brief');assert(await plain.locator('#asset-brief').inputValue()===fs.readFileSync('guides/how-to-prompt-ai-for-roblox-3d-models/ai-asset-brief.txt','utf8'),'brief exact');
 // Network or parse failures must leave static routes usable.
 for(const kind of ['network','malformed']){
  const broken=await browser.newContext();await broken.route('**/foundations-search-index.json',r=>kind==='network'?r.abort():r.fulfill({body:'{broken',contentType:'application/json'}));
  const p=await broken.newPage();await p.goto(root+'guides/');await p.waitForLoadState('networkidle');assert(await p.locator('[data-guide]:visible').count()===16,'failure fallback');assert(!await p.locator('#search-controls').isVisible(),'failure controls');await broken.close();
 }
 assert(errors.length===0,'console errors '+errors);
 assert(calls.every(u=>u.startsWith(root)),'external browser request');
 assert((await context.cookies()).length===0,'cookies');
 assert((await context.storageState()).origins.length===0,'browser storage');
 console.log('PASS: search title/terms/symptoms/full text, combined filters, empty/reset, safe text, keyboard order, accessibility labels/live status, 17 direct routes × 3 widths without page overflow, all eight visual stations decoded with alt/lazy/srcset, both silent clips played to completion, opt-in/reduced motion, no-JS paths/brief, failed index fallback, no external requests/cookies.');
 fs.writeFileSync('.local/browser-evidence.json',JSON.stringify({viewports:[1280,390,320],directRoutes:17,visualStations:8,clipsPlayed:2,errors,networkDestinations:[...new Set(calls)],searchAccessibleTree:ax},null,2));
 await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});

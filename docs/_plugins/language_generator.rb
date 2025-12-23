module Jekyll
  class LanguageGenerator < Generator
    priority :low

    def generate(site)
      # Iterate over a copy of the pages to avoiding infinite loop if we added to site.pages directly while iterating
      # though here we are adding to site.pages, so we should arguably duplicate the array first.
      
      original_pages = site.pages.dup
      puts "LanguageGenerator: Found #{original_pages.size} pages."
      
      original_pages.each do |page|
        puts "Processing page: #{page.url}"
        # Skip already generated pages or specific exclusions if needed
        next if page.data['lang'] == 'en'
        next if page.url.start_with?('/assets/')
        
        # We only want to translate pages that have dual content potential (layout: project, or specific pages)
        # For now, let's try to translate all pages unless they are explicitly excluded?
        # Or better, check if they have a layout or are html/md files.
        
        next unless page.ext == '.md' || page.ext == '.html'
        
        # Skip if permalink already indicates a specific language? 
        # Typically standard pages are just standard. 

        generate_english_page(site, page)
      end
    end

    def generate_english_page(site, original_page)
      page = original_page.dup
      page.data = original_page.data.dup
      
      # Set language
      page.data['lang'] = 'en'
      
      # Adjust URL/Permalink
      # If original is /projects/slug/, new is /en/projects/slug/
      # If original is /, new is /en/
      
      if original_page.url == '/' || original_page.url == '/index.html'
        page.data['permalink'] = '/en/'
      else
        # We need to ensure we prepend /en/ to the output path
        # If the page relies on automatic permalinks, we might need to set dir.
        
        # A simpler way for Pages in Jekyll is often setting the 'dir'.
        # However, modifying 'dir' on a duped page might be tricky if it shares internal state.
        
        # Let's try setting permalink explicitly based on the original URL.
        original_url = original_page.url
        # Ensure it doesn't double slash
        new_url = "/en#{original_url}"
        
        # Handle trailing slash logic if needed, but usually Jekyll handles it?
        # If original_url matches /projects/slug/, new is /en/projects/slug/
        
        page.data['permalink'] = new_url
      end

      # Force URL refresh (Jekyll memoizes url)
      page.instance_variable_set('@url', nil)

      # Cross-reference
      original_page.data['alternate_url'] = page.url
      original_page.data['lang'] = 'pt' # Ensure default is explicit
      
      page.data['alternate_url'] = original_page.url
      
      site.pages << page
    end
  end
end

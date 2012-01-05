metadata :name => "Java App Agent",
            :description => "Start and stop CT Java Applications",
            :author => "R.T.Nair",
            :license => "ASL2",
            :version => "1.2",
            :url => "http://cleartrip.com",
            :timeout => 200

action "status", :description => "Gets the status of a Java App" do
    display :always

    input :appname,
          :prompt => "Java App Name",
          :description => "The Java App to get the status for",
          :type => :string,
          :validation => '^[a-zA-Z\.\-_\d]+$',
          :optional => false,
          :maxlength => 90

    output "status",
          :description => "The status of the Java App",
          :display_as => "Java App Status"
end

["stop", "start", "restart"].each do |act|
    action act, :description => "#{act.capitalize} a Java App" do
        display :failed

        input :appname,
              :prompt => "Java App Name",
              :description => "The Java App to #{act}",
              :type => :string,
              :validation => '^[a-zA-Z\.\-_\d]+$',
              :optional => false,
              :maxlength => 90

        output "status",
              :description => "The status of the Java App after #{act.sub(/p$/, 'pp')}ing",
              :display_as => "Application Status"
    end
end
